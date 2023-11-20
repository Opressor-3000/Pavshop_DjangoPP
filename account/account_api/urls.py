from django.urls import path


from .viewapi import AccountAPIView, AddWishlistAPIView, ProductToBasketOldOrderAPIView, ShoppingCartAPIView, WishlistAPIView, AddToCartAPIView, OrdersAPIView
from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
   TokenVerifyView,
)
 

app_name = 'account_api'


urlpatterns = [
    # path('<int:pk>', AccountAPIView.as_view(), name='account_api'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refrash'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('', AccountAPIView.as_view(), name='account'),
    path('add_wishlist/', AddWishlistAPIView.as_view(), name='add_wishlist'),
    path('producttobasketapi/', ProductToBasketOldOrderAPIView.as_view(), name='add_producttobasket'),
    path('shopcart/', ShoppingCartAPIView.as_view(), name='shopcartapi'),
    path('wishlist/', WishlistAPIView.as_view(), name='wishlistapi'),
    path('addtocart/', AddToCartAPIView.as_view(), name='addtocartapi'),
    path('orders/', OrdersAPIView.as_view(), name='ordersapi')
]