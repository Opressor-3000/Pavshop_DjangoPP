from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View
from django.db.models.query import QuerySet
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from .tasks import send_email
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
import json


from .models import User, ProductToBasket, Address
from account.forms import RegisterForm
from .forms import RegisterForm, UserAuthForm
from .utils import account_activation_token
from .models import User
from product.models import Variant


class UserAccount(ListView):  
    model = User
    template_name = 'account/account.html'
    context_object_name = 'user'


class ActivateView(View):
    def get(self, request,  *args, **kwargs):
        uidb64 = kwargs.get("uidb64")
        token = kwargs.get("token")
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, user.DoesNotExist):
            user = None

        if user and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('account:login')
        else:
            return render(request, 'account/activation.html')


class UserRegister(CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site =get_current_site(self.request)
        send_email(user, current_site)
        return response

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:    
        return super().form_invalid(form)
    

class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'account/login.html'
    form_class = UserAuthForm

    def get_success_url(self):
        return reverse_lazy('core:homepage')
    
def login(request):
    if request.method == "POST":
        form = UserAuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data["email"], password=form.cleaned_data["password"])
            if user:
                django_login(request, user)
                return redirect(reverse_lazy("core:homepage"))
    else: form = UserAuthForm()

    context = {
        "form": form
    }

    return render(request, "account/login.html", context)
    

class Basket(LoginRequiredMixin, ListView):
    model = ProductToBasket
    template_name = 'account/shopping_cart.html'
    context_object_name = 'shopcart'

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.user.is_authenticated:
            print(self.request.user.id,"+++++")
            print(ProductToBasket.objects.filter(user=self.request.user))

            return Variant.objects.filter(variantinbasket__user=self.request.user)
       
        


class Checkout(LoginRequiredMixin, CreateView):
    model = Address
    template_name = 'account/checkout.html'


class Wishlist(LoginRequiredMixin, ListView):  
    model = User
    template_name = 'account/wishlist.html'
    context_object_name = 'wishlist'

    def add_to_wishlist(self):
        pass

@login_required
def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('account:login'))

def add_to_basket(request):
    if request.method == "POST":
        pass

def update_item(request):
    data = json.loads(request.data)
    productid = data['productId']
    action = data['action']
    user = request.user.id
    product = Variant.objects.get(id=productid)
    order, created = ProductToBasket.objects.get_or_create(user=user, order=1)

    prodtobask = 1

    order_item, created = 1

    if action == 'add':
        ProductToBasket.count += 1
    elif action == 'remove' and ProductToBasket.count > 1:
        ProductToBasket.count -= 1

    if ProductToBasket.count <= 0:
        ProductToBasket.objects.delete()

    return JsonResponse('item was added', safe=False)

