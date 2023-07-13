from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('product_detail/', product_detail, name = 'product_detail'),
    path('product_list/', product_list, name = 'product_list'),

]