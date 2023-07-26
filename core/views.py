from datetime import datetime

from django.shortcuts import render, redirect
from typing import Any, Dict
from django.db import models
from django.views.generic import ListView, DetailView, CreateView
from django.db.models.query import QuerySet

from product.models import Product, Variant, Discount
from .models import *


def about_us(request):
    return render(request, "/about_us.html")


class Contact(CreateView):
    model = Contact
    template_name = 'templates/contact.html'


# def contact(request):
#     return render("contact.html")

class HomePage(ListView):
    model = Product
    template_name = 'templates/index.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Pavshop'
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        now = datetime.now()
        return Discount.objects.annotate()


