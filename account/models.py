from django.conf import settings
from django.db import models
from django.db.models import Sum, Max, F
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models.signals import post_save
from core.Abstact_models import AbstractModel


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,
        null=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    email = models.EmailField(_("email address"), unique=True, blank=True)
    phone = models.CharField(
        max_length=20, db_index=True, unique=True, verbose_name="phone"
    )
    avatar = models.ImageField(upload_to="avatars/", blank=True)
    saller = models.BooleanField(default=False, verbose_name="Saller")
    bloger = models.BooleanField(default=False, verbose_name="Bloger")
    deleted_at = models.BooleanField(default=False, verbose_name="delete Account")

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["-pk"]

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse_lazy("user", kwargs={"user": self.id})


class Address(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    company_name = models.CharField(max_length=50, blank=True, verbose_name="Company")
    address = models.CharField(max_length=100, verbose_name="Address")
    city = models.CharField(max_length=50, verbose_name="City/Town")
    country = models.CharField(max_length=50, verbose_name="Country")
    deleted_at = models.BooleanField(default=False, verbose_name="delete at Address")

    class Meta:
        verbose_name = "user_address"
        verbose_name_plural = "addresses"
        ordering = ["-pk"]

    def __str__(self) -> str:
        return f"{self.company_name} address:{self.address}"


class Status(AbstractModel):
    title = models.CharField(
        max_length=50, unique=True, db_index=True, verbose_name="Order status"
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "status"
        verbose_name_plural = "statuses"
        ordering = ["pk"]

    def __str__(self) -> str:
        return f"{self.title}"

    def get_order_status(self, user):
        pass


class Order(AbstractModel):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="username", related_name="user_id"
    )
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, verbose_name="status", related_name="status",
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        verbose_name="delivery_address",
        related_name="address_delivery",
        blank=True,
    )

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"
        ordering = ["-pk"]

    def __str__(self) -> str:
        return f"{self.pk} {self.status}"

    @property
    def lastorder(self, user):
        userorder = Order.objects.filter(status=1, user=user)
        return userorder.aggregate(Max("id"))

    @property
    def subtotal(self, user):
        order = self.lastorder(user)
        return Variant.objects.aggregate(Sum("price")).filter(
            order__variantinptb__in=order
        )

    def alluserorder(self, user):
        pass

    def create_order(sender, **kwargs):
        if kwargs["created"]:
            user_profile = Order.objects.create(user=kwargs["instance"])

    post_save.connect(create_order, sender=User)


from product.models import Variant, Discount


class WishList(AbstractModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="user", related_name="wishlistuser"
    )
    variant = models.ForeignKey(
        Variant,
        on_delete=models.CASCADE,
        verbose_name="variant",
        related_name="wishlistvariant",
    )
    deleted_at = models.BooleanField(
        default=False, db_index=True, verbose_name="delete at from Wishlist"
    )

    class Meta:
        unique_together = ["user", "variant"]
        verbose_name = "users_wishs"
        verbose_name_plural = "wishlists"
        ordering = ["-pk"]

    def get_absolute_url(self):
        return reverse_lazy("account", kwargs={"wishlist": self.user})

    def __str__(self) -> str:
        return f"{self.user} wish:{self.variant}"


class ProductToBasket(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_basket")
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, verbose_name="Order", related_name="order"
    )
    variant = models.ForeignKey(
        Variant,
        on_delete=models.PROTECT,
        verbose_name="Variant",
        related_name="variantinbasket",
    )
    count = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Count")
    discount_id = models.ForeignKey(
        Discount,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="discount",
    )

    def get_list_product_from_order(self, user, status):
        order = Order.alluserorder(user, status)
        return Variant.objects.filter(variantinptb=order)

    class Meta:
        verbose_name = "product_to_basket"
        verbose_name_plural = "products_to_basket"
        ordering = ["-pk"]

    def get_absolute_url(self):
        return reverse_lazy("shopcart", kwargs={"shopcartlist": self.user})

    def __str__(self) -> str:
        return f"{self.user} {self.variant} count:{self.count}"

    def get_or_create(self):
        pass

    def get_price_fo_varinat(self):
        try:
            price = self.objects.get(variant__price=0)
        except:
            ValueError("error")
