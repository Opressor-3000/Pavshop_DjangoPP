from django.urls import path


from .views import *


app_name = 'account'


urlpatterns = [
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('wishlist/<int:pk>/', Wishlist.as_view(), name='wishlist'),
    path('addtowishlist/<slug:variant_slug>', AddToWishList.as_view(), name='addtowishlist'),
    path('login/', login, name = 'login'),
    path('register/', UserRegister.as_view(), name='register'),
    path('addtocart/<slug:variantslug>/', AddToCartView.as_view(), name='addtocart'),
    path('shopping_cart/', Basket.as_view(), name='shopcart'),
    path('logout/', logout, name='logout'),
    path('', UserAccount.as_view(), name='profile'),
    path("activate/<uidb64>/<token>/", ActivateView.as_view(), name='activation'),
    path("updateitem", update_item, name='updateitem'),
    path("password_reset/<str:uidb64>/<str:token>/",UserPasswordResetConfirmView.as_view(),name='password-reset'),
    path('forget_pwd/',UserPasswordResetView.as_view(),name='forget_pwd'),

    # path('password_change/done/', name='password_change_done'),
    # path('password_reset/', name='password_reset'),
    # path('password_change/', name='password_change'),
    # path('password_reset/done/', name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', name='password_reset_confirm'),
    # path('reset/done/', name='password_reset_complete'),
]
