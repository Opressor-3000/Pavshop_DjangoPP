from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.db.models.query import QuerySet


from .models import Variant, Product


class ProductDetail(DetailView):
    model = Variant
    template_name = 'templates/product_detail.html'


class ProductList(ListView):
    model = Variant
    template_name = 'templates/product.html'


class Category(ListView):
    model = Product
    template_name = 'template/product.html'


class Brand(ListView):
    model = Product
    template_name = 'template/product.html'


class Style(ListView):
    model = Product
    template_name = 'template/product.html'


class Discont(ListView):
    model = Variant
    template_name = 'template/product.html'


# def product_detail(request):
#     return render("product_detail.html")

# def product_list(request):
#     return render("product_list.html")