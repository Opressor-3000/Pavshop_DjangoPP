from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


from core.Abstact_models import AbstractModel


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=20, db_index=True, unique=True,verbose_name='phone')
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    saller = models.BooleanField(default=False, verbose_name='Saller')
    bloger = models.BooleanField(default=False, verbose_name='Bloger')
    deleted_at = models.BooleanField(default=False, verbose_name='delete Account')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-pk']

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        return self.username
    
    def get_absolute_url(self):
        return reverse_lazy('account', kwargs={'account': [self.first_name, self.last_name]})


class Address(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    company_name = models.CharField(max_length=50, blank=True, verbose_name='Company')
    address = models.CharField(max_length=100, verbose_name='Address')
    city = models.CharField(max_length=50, verbose_name='City/Town')
    country = models.CharField(max_length=50, verbose_name='Country')
    deleted_at = models.BooleanField(default=False, verbose_name='delete at Address')

    class Meta:
        verbose_name = 'user_address'
        verbose_name_plural = 'addresses'
        ordering = ['-pk']

    def __str__(self) -> str:
        return f'{self.company_name} address:{self.address}'

   
class Status(AbstractModel):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Order status')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'
        ordering = ['pk']

    def __str__(self) -> str:
        return f'{self.title}'

        
class Order(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='username', related_name='user_id')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='status', related_name='status')
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name='delivery_address', related_name='address_delivery')

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders' 
        ordering = ['-pk']

    def __str__(self) -> str:
        return f'{self.pk} {self.status}'


from product.models import Variant, Discount

    
class WishList(AbstractModel):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user', related_name='wishlistuser')
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, verbose_name='variant', related_name='wishlistvariant')
    deleted_at = models.BooleanField(default=False, db_index=True, verbose_name='delete at from Wishlist')

    class Meta:
        unique_together = ['user', 'variant']
        verbose_name = 'users_wishs'
        verbose_name_plural = 'wishlists'
        ordering = ['-pk']

    def get_absolute_url(self):
        return reverse_lazy('account', kwargs={'account': [self.first_name, self.last_name]})
    
    def __str__(self) -> str:
        return f'{self.user} wish:{self.variant}'


class ProductToBasket(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Order', related_name='order')
    variant = models.ForeignKey(Variant, on_delete=models.PROTECT, verbose_name='Variant', related_name='variant')
    count = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Count')
    discount_id = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True, verbose_name='discount')

    class Meta:
        verbose_name = 'product_to_basket'
        verbose_name_plural = 'products_to_basket'
        ordering = ['-pk']

    def __str__(self) -> str:
        return f'{self.user} {self.variant} count:{self.count}'
    

