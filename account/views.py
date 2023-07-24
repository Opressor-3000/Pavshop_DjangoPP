from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.db.models.query import QuerySet


from .models import User, ProductToBasket, Address
from core import urls


class UserAccount(DeleteView):
    model = User
    template_name = 'templates/account.html'
    context_object_name = 'account'

class UserRegister(CreateView):
    model = User
    template_name = 'templates/register.html'
    context_object_name = 'user'


class UserAuth(CreateView):
    model = User
    template_name = 'tamplates/login.html'


class Basket(ListView):
    model = ProductToBasket
    template_name = 'templates/shopping_cart.html'


class Checkout(CreateView):
    model = Address
    template_name = 'templates/checkout.html'


def logout(request):
    return render('index.html')

# def checkout(request):
#     return render("checkout.html")

# def login(request):
#     return render("login.html")

# def register(request):
#     return render("register.html")

# def shopping_cart(request):
#     return render("shopping_cart.html")

