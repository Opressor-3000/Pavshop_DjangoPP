from datetime import datetime


from django.shortcuts import render, redirect
from typing import Any, Dict
from django.db import models
from django.views.generic import ListView, DetailView, CreateView
from django.db.models.query import QuerySet


from product.models import Product, Variant, Discount, Category, Brand, Style
from .models import *
from core.templatetags.nav_tags import get_discount


def about_us(request):
    return render(request, "core/about-us.html")


class Contact(CreateView):
    model = Contact
    template_name = 'core/contact.html'

# def contact(request):
#     return render("contact.html")


class HomePage(ListView):
    paginate_by = 9
    model = Variant
    template_name = 'core/index.html'
    context_object_name = 'toplist'
    allow_empty = True

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        discount = get_discount()
        discount_prod = Variant.objects.filter(discount_id__in = discount)
        context['discount_prod']=discount_prod[:3]
   
        # context['discount'] = Variant.objects.filter(discount_id=discount).order_by('-discount_id__created_at')[:3]
        return context
    
    def get_queryset(self) -> QuerySet[Any]:    
        variants = Variant.objects.filter(varianttostore__quantity__gte = 1)
        return variants
    


