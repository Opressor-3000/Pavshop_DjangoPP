from django.contrib import admin

from .models import *







admin.site.register(User, Basket, ShoppingCart, Wishlist, Address, Order)
