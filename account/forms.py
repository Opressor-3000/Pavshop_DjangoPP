from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


from .models import *
from product.models import Discount   


class RegisterForm:
    
    password2 = forms.CharField(widget=forms.PasswordInput())
    # attrs={"class": "col-md-6", "placeholder": "Enter confirm password"}
    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone", "email", "password1", "password2")

    def clean(self):
        data = self.cleaned_data
        if data['password1'] != data["password2"]:
            self.add_error("password2", "Confirm password does not match")
        
        return super().clean()


class UserRegister(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'password1', 'password2']


class LogInAccount(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['email', 'password']


class UserWishList(forms.ModelForm):
    class Meta:
        model = WishList
        fields = ['variant']


class Address(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['user', 'company_name', 'address', 'city', 'country']


class DiscountCode(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['code']


class Shopcart(forms.ModelForm):
    class Meta:
        model = ProductToBasket
        fields = ['variant']

