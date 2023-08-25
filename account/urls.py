from django.urls import path


from .views import *


app_name = 'account'


urlpatterns = [
    path('checkout/', Checkout.as_view(), name = 'checkout'),
    path('login/', UserAuth.as_view(), name = 'login'),
    path('register/', register, name = 'register'),
    path('shopping_cart/', Basket.as_view(), name = 'shopcart'),
    path('logout/', logout, name='logout'),
    path('<slug:account>/', UserAccount.as_view(), name = 'account')
]

