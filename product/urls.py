from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('product/<slug:product_id>/', ProductDetail.as_view(), name = 'product'),
    path('products/', ProductList.as_view(), name = 'product_list'),
    path('category/<slug:category_id>/', Category.as_view(), name='category'),
    path('brand/<slug:brand_id>/', Brand.as_view(), name='brand'),
    path('style/<slug:style_id>/', Style.as_view(), name='style'),
    path('discont/<slug:discont>/', Discont.as_view(), name='discont')

]