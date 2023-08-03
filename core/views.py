from datetime import datetime

from django.shortcuts import render, redirect
from typing import Any, Dict
from django.db import models
from django.views.generic import ListView, DetailView, CreateView
from django.db.models.query import QuerySet

from product.models import Product, Variant, Discount, Category, Brand, Style
from .models import *


def about_us(request):
    return render(request, "core/about-us.html")


class Contact(CreateView):
    model = Contact
    template_name = 'templates/contact.html'

# def contact(request):
#     return render("contact.html")


class HomePage(ListView):
    # paginate_by = 8
    model = Product
    template_name = 'templates/index.html'
    context_object_name = 'toplist'
    allow_empty = False

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return Variant.objects.filter(quantity__gt = 1).order_by('-created_at')
    


