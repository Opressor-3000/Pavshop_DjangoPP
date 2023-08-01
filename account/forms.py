from django import forms


from .models import *
from product.models import Discount


class NewUserAccount(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'password', 'password', 'avatar']


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
        fields = ['first_name', 'last_name', 'compzny_name', 'address', 'city', 'country', 'email', 'phone']


class DiscountCode(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['code']


class Shopcart(forms.ModelForm):
    class Meta:
        model = ProductToBasket
        fields = ['variant']

