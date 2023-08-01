from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models.query import QuerySet


from .models import Variant, Product
from core.utils import BaseMixin


class ProductDetail(BaseMixin, DetailView):
    paginate_by = 5
    model = Variant
    template_name = 'templates/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        mainmenu = self.get_mainmenu_context()
        variants = Variant.objects.filter(product_id=context.product_id).count()

        return dict(list(context.item()) + list(mainmenu.items()))


class ProductList(BaseMixin, ListView):
    paginate_by = 9
    model = Variant
    template_name = 'templates/product_list.html'
    context_object_name = 'variants'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        mainmenu = self.get_mainmenu_context()
        return dict(list(context.item()) + list(mainmenu.items()))
    
    def get_queryset(self) -> QuerySet[Any]:
        return Variant.objects.all().order_by('-created_at')
    

class DiscountList(BaseMixin, ListView):
    paginate_by = 9
    model = Variant
    template_name = 'templates/product_list.html'
    content_type = 'products'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        mainmenu = self.get_mainmenu_context()
        return dict(list(context.item()) + list(mainmenu.items()))
    
    def get_queryset(self) -> QuerySet[Any]:
        return Variant.objects.filter(discount_id__pk = True).order_by('-created_at')


class Category(BaseMixin, ListView):
    model = Product
    template_name = 'template/product_list.html'
    context_object_name = 'products'

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.filter(category_id__slug = self.kwargs['category_id'])

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        mainmenu = self.get_mainmenu_context()
        return dict(list(context.item()) + list(mainmenu.items()))
    

class Brand(BaseMixin, ListView):
    model = Product
    template_name = 'template/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        mainmenu = self.get_mainmenu_context()
        return dict(list(context.item()) + list(mainmenu.items()))


class Style(BaseMixin, ListView):
    model = Product
    template_name = 'template/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        mainmenu = self.get_mainmenu_context()
        return dict(list(context.item()) + list(mainmenu.items()))


class Collection(BaseMixin, ListView):
    model = Product
    template_name = 'templates/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        mainmenu = self.get_mainmenu_context()
        return dict(list(context.item()) + list(mainmenu.items()))

