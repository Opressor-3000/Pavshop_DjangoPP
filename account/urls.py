from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('checkout/', checkout, name = 'checkout'),
    path('login/', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('shopping_cart/', shopping_cart, name = 'shopping_cart')
]