from django import forms


from .models import *


class NewUserAccount(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'surname', 'phone', 'password', 'password']


class UserWishList(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['product_id']


class ShoppingCart(forms.ModelForm):
    class Meta:
        model = ShoppingCart
        fields = ['basket_id']


class Address(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['first_name', 'last_name', 'compzny_name', 'address', 'city', 'country', 'email', 'phone']



