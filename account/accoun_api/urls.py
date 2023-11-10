from django.urls import path


from .viewapi import AccountAPIView,AddWishlistAPIView
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
    path('user/', AccountAPIView.as_view(), name='account'),
    path('add_wishlist/', AddWishlistAPIView.as_view(), name='add_wishlist')
]