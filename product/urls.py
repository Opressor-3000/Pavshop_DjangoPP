from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('product_detail/<slug:product_id>/', ProductDetail.as_view(), name = 'product_detail'),
    path('product_list/', ProductList.as_view(), name = 'product_list'),

]