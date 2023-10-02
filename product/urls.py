from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('<slug:variant_slug>/', ProductDetail.as_view(), name = 'product'),
    path('', ProductList.as_view(), name = 'product_list'),
]