from django.shortcuts import render
from typing import Any, Dict
from django.db import models
from django.views.generic import ListView, DetailView, CreateView
from django.db.models.query import QuerySet

from product.models import Variant

def about_us(request):
    return render("about_us.html")

def contact(request):
    return render("contact.html")

class HomePage(ListView):
    model = Variant
    template_name = 'templates/index.html'


    