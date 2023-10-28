from datetime import datetime


from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models.query import QuerySet
from django.db.models import Q, Sum, Count
from rest_framework import generics


from .serializers import ProductSerializer
from .models import Variant, Product, Image, Category, Color, Tag
from .utils import count_variant, get_current_discount
# from core.templatetags.nav_tags import get_discount


class ProductDetail(DetailView):
    model = Variant
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'variant_slug'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['variants'] = Variant.objects.filter(product_id__variantofproduct=kwargs["object"].id)
        return context

class ProductList(ListView):
    paginate_by = 9
    model = Variant
    template_name = 'product/product_list.html'
    context_object_name = 'variants'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(parent=None)
        context['colours'] = Color.objects.all()
        context['tags'] = Tag.objects.all()[:9]
        return context


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
            if req.get('discounts'):
                discount = get_current_discount()
                queryset = queryset.filter(discount_id__in=discount)
            if req.getlist('brand'):
                queryset = queryset.filter(product_id__brand_id__slug__in=req.getlist('brand'))
            if req.getlist('style'):
                queryset = queryset.filter(product_id__style_id__slug__in=req.getlist('style'))
            if req.getlist('color'):
                queryset = queryset.filter(color__title__in=req.getlist('color'))
            if req.getlist('unit'):
                queryset = queryset.filter(unit__in=req.getlist('unit'))
            if req.getlist('tag'):
                queryset = queryset.filter(tag__in=req.getlist('tag'))
            if req.getlist('category'):
                queryset = queryset.filter(product_id__category_id__title__in=req.getlist('category'))
            if req.getlist('minprice'):
                queryset = queryset.filter(price__gte=req.get('minprice'))
            if req.getlist('maxprice'):
                queryset = queryset.filter(price__lte=req.get('maxprice'))
            if req.get('new_arrival'):
                queryset = queryset.order_by('-created_at')
            elif req.get('old_arrival'):
                queryset = queryset.order_by('created_at')
            elif req.get('popular'):
                queryset = queryset.filter(variantinbasket__order=2).annotate(total_count = Sum('variantinbasket__count')).order_by('total_count')
            return queryset
            
