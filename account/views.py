from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.db.models.query import QuerySet


from .models import User, ProductToBasket, Address
from account.forms import RegisterForm
from .forms import RegisterForm
from core import urls


# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST, files=request.FILES)
#         if form.is_valid():
#             user = form.save()
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect(reverse_lazy('core:homepage'))
#     else:
#         form = RegisterForm

#     context = {
#         "form": form
#     }

#     return render(request, 'account/register.html', context)


class UserAccount(DeleteView):  
    model = User
    template_name = 'account/account.html'
    context_object_name = 'account'

class UserRegister(CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('account/login')
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        print(request.POST)
        return super().post(request, *args, **kwargs)
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        print(2)
        print(form.errors)
        return super().form_invalid(form)

class UserAuth(CreateView):
    model = User
    template_name = 'account/login.html'
    context_object_name = 'data'


class Basket(ListView):
    model = ProductToBasket
    template_name = 'account/shopping_cart.html'
    context_object_name = 'shopcart'


class Checkout(CreateView):
    model = Address
    template_name = 'account/checkout.html'



class Wishlist(ListView):  
    model = User
    template_name = 'account/wishlist.html'
    context_object_name = 'wishlist'


def logout(request):
    return render('index.html')

