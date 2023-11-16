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
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,TemplateView
from django.contrib import messages


from .models import User, ProductToBasket, Address, WishList, Order
from account.forms import RegisterForm
from .forms import RegisterForm, UserAuthForm, AddToCartForm, UserPasswordResetConfirmForm, UserPasswordResetForm
from .utils import account_activation_token
from product.models import Variant, ProductReview
from core.templatetags.shopcart_tags import get_shopcarts



class UserAccount(ListView):  
    model = User
    template_name = 'account/account.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['sopping_cart'] = get_shopcarts(self.request)
        context['user_reviews'] = ProductReview.objects.filter(user=self.request.user)
        return context
    

class UserAccountAPI(ListView):  
    model = User
    template_name = 'account/account_api.html'
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
    

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'account/login.html'
    form_class = UserAuthForm
    
    def get_success_url(self):
        return reverse_lazy('core:homepage')

    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


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
            return Variant.objects.filter(variantinbasket__user=self.request.user)
       
    
class Checkout(LoginRequiredMixin, ListView):   # способы оплаты
    model = ProductToBasket
    template_name = 'account/checkout.html'
    context_object_name = 'checkout'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(order__status__id=1)
    
    


class AddToCartView(LoginRequiredMixin, CreateView):    #  добавить в корзину 
    form_class = AddToCartForm
    template_name = 'product/product_detail.html'
    success_url = reverse_lazy('product:product')

    def get_addtocart(self, *, object_list=None, **kwargs):
        if self.request.user.is_authenticated:
            user = self.request.user.id
            if Order.objects.filter(user=self.request.user, status=1):
                pass
            #     product_to_basket, created = ProductToBasket.objects.get_or_create(user=user, count=1)
            else:
                order = Order.objects.create(user=user, status=1)
                # self.get_addtocart(object_list=None, **kwargs)
        # else:

        # if Order.objects.filter(user=self.request.user).filter(status=2).first():
        #     1
        # else:
        #     2



class AddToWishList(LoginRequiredMixin, CreateView):
    # form_class = AddToWhishlistForm
    template_name = 'account/add_wishlist.html'

    def get_success_url(self) -> str:
        return self.request.GET.get('next')


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
    if action == 'add':
        ProductToBasket.count += 1
    elif action == 'remove' and ProductToBasket.count > 1:
        ProductToBasket.count -= 1

    if ProductToBasket.count <= 0:
        ProductToBasket.objects.delete()

    return JsonResponse('item was added', safe=False)


class UserPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset_form.html'
    form_class=UserPasswordResetForm
    email_template_name = 'account/password-reset.html'
    success_url = reverse_lazy('account:forget_pwd')
    
    def get_success_url(self):
         messages.add_message(self.request, messages.INFO, 'Parolunuzu yenilemek haqqinda istey mailinize gonderilmistir')
         return self.success_url


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    form_class=UserPasswordResetConfirmForm
    success_url=reverse_lazy("account:login")

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Parolunuz deyisildi')
        return self.success_url

class AccountView(LoginRequiredMixin, View):
    model = User
    template_name = 'account/account_api.html'
    context_object_name = 'user'

    