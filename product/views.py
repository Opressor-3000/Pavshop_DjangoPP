from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models.query import QuerySet
from rest_framework import generics


from .serializers import ProductSerializer
from .models import Variant, Product
from core.utils import BaseMixin


class ProductDetail(BaseMixin, DetailView):
    model = Variant
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # request  = kwargs['request']
        variants = Variant.objects.all()
        # if request.GET.get('color',):
        #     products.filter(color__in=request.GET.get('color',''))
        # if request.GET.get('brand',):
        #     products.filter(brand__in=request.GET.get('brand',''))
        context = {
            variants : 'variants'
        }
        return context


class ProductList(BaseMixin, ListView):
    paginate_by = 9
    model = Variant
    template_name = 'product/product_list.html'
    context_object_name = 'variants'

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return Variant.objects.all().order_by('-created_at')


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
