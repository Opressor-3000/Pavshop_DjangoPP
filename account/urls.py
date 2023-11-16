from django.urls import path


from .views import *


app_name = 'account'


urlpatterns = [
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('wishlist/', Wishlist.as_view(), name='wishlist'),
    path('addtowishlist/<slug:variant_slug>', AddToWishList.as_view(), name='addtowishlist'),
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('register/', UserRegister.as_view(), name='register'),
    path('addtocart/<slug:variantslug>/', AddToCartView.as_view(), name='addtocart'),
    path('shopping_cart/', Basket.as_view(), name='shopcart'),
    path('logout/', logout, name='logout'),
    path('', UserAccount.as_view(), name='profile'),
    path("activate/<uidb64>/<token>/", ActivateView.as_view(), name='activation'),
    path("producttobasket/", update_item, name='producttobasket'),
    path("password_reset/<str:uidb64>/<str:token>/",UserPasswordResetConfirmView.as_view(),name='password_reset'),
    path('forget_pwd/',UserPasswordResetView.as_view(), name='forget_pwd'),
    path('user/', AccountView.as_view(), name='api_account'),
    path('profile/', UserAccountAPI.as_view(), name='profile'),
]
