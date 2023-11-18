from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('<slug:variant_slug>/', ProductDetail.as_view(), name = 'product'),
    path('', ProductList.as_view(), name='productlist'),
    path('', ProductListFetch.as_view(), name = 'product_list'),
    path('add_item/', updateItem, name = 'update'),
]