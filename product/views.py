from datetime import datetime
import json

from typing import Any, Dict
from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.db.models.query import QuerySet
from django.db.models import Q, Sum, Count
from rest_framework import generics
from django.http import JsonResponse
from account.models import ProductToBasket, Order



from .models import Variant, Category, Color, Tag, Brand
from .utils import count_variant, get_current_discount, get_subcat, get_parent
from account.forms import ProductReviewForm


def updateItem(request):    
    data = json.loads(request.data)
    variant = data['productId']
    action = data['action']
    user = request.user.id

    order = Order.objects.filter(user=user, status=2)
    add_to_basket = ProductToBasket.objects.create(user=user, variant=variant, order=order)

    if action == 'add':
        add_to_basket.count = add_to_basket.count + 1 
    elif action == 'remove':
        add_to_basket.count = add_to_basket.count -1
    return JsonResponse('Item was added!', safe=False)


class ProductDetail(FormMixin, DetailView):
    model = Variant
    template_name = 'product/product_detail.html'
    form_class = ProductReviewForm
    context_object_name = 'product'
    slug_url_kwarg = 'variant_slug'
    
    def get_success_url(self, **kwargs):         
        if  kwargs != None:
            return reverse_lazy('product:product', kwargs = {'variant_slug': self.slug})

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['variants'] = Variant.objects.filter(product_id__variantofproduct=kwargs["object"].id)
        if not Variant.objects.filter(variantinbasket__order__status_id=2):
            context['popular_prod'] = Variant.objects.all().order_by('-created_at')
        else:
            context['popular_prod'] = Variant.objects.filter(variantinbasket__order__status_id=2).annotate(total_count = Sum('variantinbasket__count')).order_by('total_count')
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        form.instance.product=self.get_object().product_id
        form.instance.user = self.request.user
        form.instance.rating=4
        form.save()
        return super().form_valid(form)
    

class ProductListFetch(ListView):
    paginate_by = 6
    model = Variant
    template_name = 'product/product_list.html'
    context_object_name = 'variants'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = get_subcat()
        context['colours'] = Color.objects.all()
        context['tags'] = Tag.objects.all()[:9]
        context['brands'] = Brand.objects.all()[:9]
        print('-------------------------------------------------------------------------------')
        return context
        

class ProductList(ListView):
    paginate_by = 6
    model = Variant
    template_name = 'product/productlist.html'
    context_object_name = 'variants'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = get_subcat()
        context['colours'] = Color.objects.all()
        context['tags'] = Tag.objects.all()[:9]
        context['brands'] = Brand.objects.all()[:9]
        return context
    
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
                queryset = queryset.filter(tag__title__in=req.getlist('tag'))
            if req.getlist('category'):
                queryset = queryset.filter(product_id__category_id__slug__in=req.getlist('category'))
            if req.getlist('minprice'):
                queryset = queryset.filter(price__gte=req.get('minprice'))
            if req.getlist('maxprice'):
                queryset = queryset.filter(price__lte=req.get('maxprice'))
            if req.get('new_arrival'):
                queryset = queryset.order_by('-created_at')
            elif req.get('old_arrival'):
                queryset = queryset.order_by('created_at')
            elif req.get('popular'):
                if queryset.filter(variantinbasket__order__status_id=2):
                    queryset = queryset.filter(variantinbasket__order__status_id=2).annotate(total_count = Sum('variantinbasket__count')).order_by('total_count')
                else:
                    queryset = queryset.order_by('-created_at')
            return queryset
            
