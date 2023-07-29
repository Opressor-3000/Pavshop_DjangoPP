from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models.query import QuerySet


from .models import Variant, Product
from core.utils import BaseMixin


class ProductDetail(BaseMixin, DetailView):
    paginate_by = 8
    model = Variant
    template_name = 'templates/product_detail.html'


class ProductList(BaseMixin, ListView):
    paginate_by = 9
    model = Variant
    template_name = 'templates/product.html'
    context_object_name = 'variants'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        mainmenu = self.get_mainmenu_context()
        return dict(list(context.item()) + list(mainmenu.items()))
    
    def get_queryset(self) -> QuerySet[Any]:
        return Variant.objects.all().order_by('-created_at')
    

class DiscountList(BaseMixin, ListView):
    paginate_by = 8
    model = Variant


class Category(BaseMixin, ListView):
    model = Product
    template_name = 'template/product.html'
    context_object_name = 'producttocategory'

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.filter(category_id__slug = self.kwargs['category_id'])


class Brand(BaseMixin, ListView):
    model = Product
    template_name = 'template/product.html'


class Style(BaseMixin, ListView):
    model = Product
    template_name = 'template/product.html'


class Discont(BaseMixin, ListView):
    model = Variant
    template_name = 'template/product.html'


# def product_detail(request):
#     return render("product_detail.html")

# def product_list(request):
#     return render("product_list.html")