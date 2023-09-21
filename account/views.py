from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, View
from django.db.models.query import QuerySet
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from .tasks import send_email
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode


from .models import User, ProductToBasket, Address
from account.forms import RegisterForm
from .forms import RegisterForm, UserAuthForm
from core import urls
from .utils import account_activation_token
from .models import User


class UserAccount(DeleteView):  
    model = User
    template_name = 'account/account.html'
    context_object_name = 'user'


class ActivateView(View):
    def get(self, request,  *args, **kwargs):
        uidb64 = kwargs.get("uidb64")
        token = kwargs.get("token")
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.object.get(pk=uid)
        except(TypeError, ValueError, OverflowError, user.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('account:login')
        else:
            return render(request, 'activation.html')


class UserRegister(CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('account/login')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = self.request.META['HTTP_HOST']
        send_email(user, current_site)

        return response

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        print(request.POST)
        return super().post(request, *args, **kwargs)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:    
        return super().form_invalid(form)
    

class LoginView(LoginView):
    model = User
    form_class = UserAuthForm
    template_name = 'account/login.html'
    context_object_name = 'data'


class Basket(ListView):
    model = ProductToBasket
    template_name = 'account/shopping_cart.html'
    context_object_name = 'shopcart'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()


class Checkout(CreateView):
    model = Address
    template_name = 'account/checkout.html'


class Wishlist(ListView):  
    model = User
    template_name = 'account/wishlist.html'
    context_object_name = 'wishlist'


def logout(request):
    return render('index.html')

