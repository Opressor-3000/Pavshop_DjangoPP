from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models.query import QuerySet
from django.db.models import Q
from rest_framework import generics


from .serializers import ProductSerializer
from .models import Variant, Product
# from core.templatetags.nav_tags import get_discount


class ProductDetail(DetailView):
    model = Variant
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'variant_slug'


class ProductList(ListView):
    paginate_by = 9
    model = Variant
    template_name = 'product/product_list.html'
    context_object_name = 'variants'
    
    def get_queryset(self) -> QuerySet[Any]:
        req = self.request.GET
        discount = 1
        if req.getlist:
            return Variant.object.filter(color__in=())
        if req.getlist['color']:
            color = req.getlist['color']
            color = Variant.objects.filter(color__in=color)
        if req.getlist['discount']:
            discount = Variant.objects.filter(discount__in=req.getlist['discount']) 
        if req.getlist['unit']:
            unit = Variant.objects.filter(unit__in=req.getlist['unit'])
        if req.getlist['tag']:
            tag = Variant.objects.filter(tag__in=req.getlist['tag'])
        if req.getlist['category']:
            cat = Variant.objects.filter(product__category_id__in=req.getlist['category'])
"""

    In Variant
                color
                discount
                unit
                tag
    In Product 
                category
                collection
                brand
                desifner
                style

"""

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
