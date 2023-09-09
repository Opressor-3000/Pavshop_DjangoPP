from django.urls import path


from .views import *


app_name = 'account'


urlpatterns = [
    path('checkout/', Checkout.as_view(), name = 'checkout'),
    path('wishlist/<int:pk>/', Wishlist.as_view(), name = 'wishlist'),
    path('login/', UserAuth.as_view(), name = 'login'),
    path('register/', UserRegister.as_view(), name='register'),
    path('shopping_cart/<int:pk>/', Basket.as_view(), name = 'shopcart'),
    path('logout/<int:pk>/', logout, name='logout'),
    path('<int:pk>/', UserAccount.as_view(), name = 'user')
]

