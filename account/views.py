from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.db.models.query import QuerySet


from .models import User, ShoppingCart


class UserRegister(CreateView):
    model = User
    template_name = 'templates/register.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        # context = super(UserRegister, self).get_context_data(**kwargs)
        # context['title'] = 'value'
        return super().get_context_data(**kwargs)
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()

class UserAuth(CreateView):
    model = User
    template_name = 'tamplates/login.html'



class ShopCart(ListView):
    model = ShoppingCart
    template_name = 'templates/shopping_cart.html'




def checkout(request):
    return render("checkout.html")

# def login(request):
#     return render("login.html")

# def register(request):
#     return render("register.html")

# def shopping_cart(request):
#     return render("shopping_cart.html")

