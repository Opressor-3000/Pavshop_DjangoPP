from datetime import datetime


from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models.query import QuerySet
from django.db.models import Q, Sum
from rest_framework import generics


from .serializers import ProductSerializer
from .models import Variant, Product, Discount
from core.utils import count_variant, get_discount
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

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)

    def exist_product(self):
        return Variant.objects.filter()
    
    def get_queryset(self) -> QuerySet[Any]:
        if self.request.method == 'GET':
            queryset = count_variant()
            req = self.request.GET
            if req.get('search'):
                queryset = queryset.filter(
                    Q(title__icontains=req.get('search')) | 
                    Q(product_id__brand_id__title__icontains=req.get('search')) |
                    Q(product_id__collection_id__title__icontains=req.get('search')) | 
                    Q(product_id__title__icontains=req.get('search')) | 
                    Q(product_id__style_id__title__icontains=req.get('search')) | 
                    Q(color__title__icontains=req.get('search')) | 
                    Q(product_id__category_id__title__icontains=req.get('search')) | 
                    Q(tag__title__icontains=req.get('search')) | 
                    Q(product_id__tag__title__icontains=req.get('search'))
                ).distinct()
            if req.get('discount'):
                discount = get_discount()
                queryset = queryset.filter(discount_id__in=discount)[:3]
            if req.getlist('brand'):
                queryset = queryset.filter(product_id__brand_id__title__in=req.getlist('brand'))
            if req.getlist('style'):
                queryset = queryset.filter(product_id__style_id__slug__contains=req.getlist('style'))
            # if req.getlist('store'):
            #     queryset = queryset.varianttostore__varianttostore.filter(quantity__gt=req.getlist('store'))
            if req.getlist('color'):
                queryset = queryset.filter(color__title__in=req.getlist('color'))
            if req.getlist('discount'):
                queryset = queryset.filter(discount__in=req.getlist('discount')) 
            if req.getlist('unit'):
                queryset = queryset.filter(unit__in=req.getlist('unit'))
            if req.getlist('tag'):
                queryset = queryset.filter(tag__in=req.getlist('tag'))
            if req.getlist('category'):
                queryset = queryset.filter(product_id__category_id__in=req.getlist('category'))
            if req.getlist('minprice'):
                queryset = queryset.filter(price__gte=req.get('minprice'))
            if req.getlist('maxprice'):
                queryset = queryset.filter(price__lte=req.get('maxprice'))
            if req.get('new_arrival'):
                queryset = queryset.order_by('-created_at')
            elif req.get('old_arrival'):
                queryset = queryset.order_by('created_at')
            elif req.get('popular'):
                queryset = queryset.annotate(total_count = Sum('variant__count')).filter(variant__order=2).order_by('total_count')
            return queryset
            
            
        
#          return Model.objects.filter(column1 = self.kwargs['postfixname'))
            
"""
    Sort_by :  
                price, discount, popular(order), add_date, review_count, rating

    Filter_by: 
                brand, collection, category, discount, style, color, unit(комплекты / шт) , tag, designer

    In Variant
                color
                discount
                unit
                tag
    In Product 
                category
                collection
                brand
                designer
                style


testargs = request.GET.getlist('testargs')   
# getlist gets all parameters with same name!!!!



# constructing the url:

>>> from django.http import QueryDict
>>> q = QueryDict(‘artists=1′).copy()
>>> my_artists = [11,22,33,44]
>>> q.setlist(‘artists’, my_artists)
>>> print q
<QueryDict: {u’artists’: [11, 22, 33, 44]}>
>>> print q.urlencode()
artists=11&artists=22&artists=33&artists=44

"""


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

