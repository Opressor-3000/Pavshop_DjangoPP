from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('product/<slug:product_id>/', ProductDetail.as_view(), name = 'product'),
    path('products/', ProductList.as_view(), name = 'product_list'),

]