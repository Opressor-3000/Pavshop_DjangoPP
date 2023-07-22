from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from core.models import AbstractModel

class User(AbstractUser):
    phone = models.CharField(max_length=20, db_index=True, unique=True)
    avatar = models.ImageField(upload_to='avatars/')
    



from product.models import Variant, Discount


class Basket(AbstractModel):
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    count = models.DecimalField(max_digits=10, decimal_places=3)
    discont_id = models.ForeignKey(Discount, on_delete=models.CASCADE)


class WishList(AbstractModel):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)

class Address(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, blank=True, verbose_name='Company')
    address = models.CharField(max_length=100, verbose_name='Address')
    city = models.CharField(max_length=50, verbose_name='City/Town')
    country = models.CharField(max_length=50, verbose_name='Country')
   
class Status(AbstractModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Order status')
  
class Order(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket = models.ManyToManyField(Basket)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    

