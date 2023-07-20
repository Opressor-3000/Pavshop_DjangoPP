from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.db.models.query import QuerySet


from .models import Variant


class ProductDetail(DetailView):
    model = Variant
    template_name = 'templates/product_detail.html'


class ProductList(ListView):
    model = Variant
    template_name = 'templates/product.list'



# def product_detail(request):
#     return render("product_detail.html")

# def product_list(request):
#     return render("product_list.html")