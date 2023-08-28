from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.db.models.query import QuerySet


from .models import User, ProductToBasket, Address
from .forms import RegisterForm
from core import urls


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(reverse_lazy('core:homepage'))
    else:
        form = RegisterForm

    context = {
        "form": form
    }

    return render(request, 'account/register.html', context)


class UserAccount(DeleteView):  
    model = User
    template_name = 'account/account.html'
    context_object_name = 'account'

class UserRegister(CreateView):
    model = User
    template_name = 'account/register.html'
    context_object_name = 'user'


class UserAuth(CreateView):
    model = User
    template_name = 'account/login.html'


class Basket(ListView):
    model = ProductToBasket
    template_name = 'account/shopping_cart.html'


class Checkout(CreateView):
    model = Address
    template_name = 'account/checkout.html'


def logout(request):
    return render('index.html')

