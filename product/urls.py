from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('<slug:product_name>/', ProductDetail.as_view(), name = 'product'),
    path('', ProductList.as_view(), name = 'product_list'),
    # path('category/<slug:style_name>/', Style, name='stule')

]