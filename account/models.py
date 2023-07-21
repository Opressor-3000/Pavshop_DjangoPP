from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from product.models import Variant, Discount


class User(models.Model):
    email = models.EmailField(unique=True, db_index=True)
    name = models.CharField(max_length=50, db_index=True)
    surname = models.CharField(max_length=50, db_index=True)
    phone = models.CharField(max_length=20, db_index=True, unique=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='User')
    password = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/%Y-%d-%B-%H-%i')
    address_id = models.ForeignKey('Address', on_delete=models.PROTECT)
    wishlist = models.ManyToManyField(Variant, unique=True, db_index=True, verbose_name='Wishlist')
    shoppingcart = models.ManyToManyField('Basket', db_index=True, verbose_name='Basket')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    

    def save(self, *args, **kwargs):
        if not self.id:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)



# class Wishlist(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)


class Basket(models.Model):
    variant_id = models.ForeignKey(Variant, on_delete=models.CASCADE)
    count = models.DecimalField(decimal_places=3)
    discont_id = models.ForeignKey(Discount, on_delete=models.CASCADE)


# class ShoppingCart(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)


class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    company_name = models.CharField(max_length=50, blank=True, verbose_name='Company')
    address = models.CharField(max_length=100, verbose_name='Address')
    city = models.CharField(max_length=50, verbose_name='City/Town')
    country = models.CharField(max_length=50, verbose_name='Country')
    email = models.EmailField()
    phone = models.CharField(max_length=20, unique=True, verbose_name='Phone')
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Status(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Order status')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shopcart_id = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)



    