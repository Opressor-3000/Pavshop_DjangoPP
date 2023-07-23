from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from core.models import AbstractModel
from django.urls import reverse_lazy

class User(AbstractUser):
    phone = models.CharField(max_length=20, db_index=True, unique=True)
    avatar = models.ImageField(upload_to='avatars/')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['pk']

    def __str__(self):
        return self.first_name, self.last_name
    
    def get_absolute_url(self):
        return reverse_lazy('account', kwargs={'account': [self.first_name, self.last_name]})


from product.models import Variant, Discount


class Basket(AbstractModel):
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    count = models.DecimalField(max_digits=10, decimal_places=3)
    discont_id = models.ForeignKey(Discount, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'product_to_basket'
        verbose_name_plural = 'products_to_basket'
        ordering = ['-pk']

    


class WishList(AbstractModel):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'users_wish'
        verbose_name_plural = 'wishlists'
        ordering = ['-pk']


class Address(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, blank=True, verbose_name='Company')
    address = models.CharField(max_length=100, verbose_name='Address')
    city = models.CharField(max_length=50, verbose_name='City/Town')
    country = models.CharField(max_length=50, verbose_name='Country')

    class Meta:
        verbose_name = 'user_address'
        verbose_name_plural = 'addresses'
        ordering = ['-pk']
   
class Status(AbstractModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Order status')

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'
        
  
class Order(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket = models.ManyToManyField(Basket)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders' 
        ordering = ['-pk']
    

