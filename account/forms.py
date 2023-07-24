from django import forms


from .models import *


class NewUserAccount(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'password', 'password', 'avatar']


class UserWishList(forms.ModelForm):
    class Meta:
        model = WishList
        fields = ['variant']


class Address(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['first_name', 'last_name', 'compzny_name', 'address', 'city', 'country', 'email', 'phone']



