from django.urls import path


from .views import *
from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
   TokenVerifyView,
)

app_name = 'account'


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refrash'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('wishlist/<int:pk>/', Wishlist.as_view(), name='wishlist'),
    path('login/', login, name = 'login'),
    path('register/', UserRegister.as_view(), name='register'),
    path('shopping_cart/', Basket.as_view(), name='shopcart'),
    path('logout/', logout, name='logout'),
    path('', UserAccount.as_view(), name='profile'),
    path("activate/<uidb64>/<token>/", ActivateView.as_view(), name='activation'),
    path("updateitem", update_item, name='updateitem'),

]

    