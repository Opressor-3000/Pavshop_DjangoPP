from django.forms import TextInput, ModelForm, CharField, PasswordInput, EmailInput, EmailField
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


from .models import *
from product.models import Discount   
from core.forms import AbstractForm


class RegisterForm(UserCreationForm):
    first_name = CharField(label='First Name', widget=TextInput(attrs={"class": "col-md-6   ", "placeholder": "Enter first name"}))
    last_name = CharField(label='Last Name', widget=TextInput(attrs={"class": "col-md-6", "placeholder": "Enter last nema"}))
    phone = CharField(label='Your Phone', widget=TextInput(attrs={"class": "col-md-6", "placeholder": "Enter your phone"}))
    email = EmailField(label='Your E-mail', widget=EmailInput(attrs={"class": "col-md-6", "placeholder": "Enter your e-mail"}))
    password1 = CharField(label='Password', widget=PasswordInput(attrs={"class": "col-md-6", "placeholder": "Enter password"}))
    password2 = CharField(label='Confirm Password', widget=PasswordInput(attrs={"class": "col-md-6", "placeholder": "Enter confirm password"}))

    class Meta:
        attrs={"class": "col-md-6", "placeholder": "Enter confirm password"}
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'password1', 'password2']
        widget = {
            'first_name':TextInput(attrs={"class": "col-md-6", "placeholder": "Enter first name"}),
            'last_name':TextInput(attrs={"class": "col-md-6", "placeholder": "Enter last name"}),
            'phone':TextInput(attrs={"class": "col-md-6", "placeholder": "Enter your phone"}),
            'email':TextInput(attrs={"class": "col-md-6", "placeholder": "Enter your e-mail"}),
            'password1':PasswordInput(attrs={"class": "col-md-6", "placeholder": "Enter password"}),
            'password2':PasswordInput(attrs={"class": "col-md-6", "placeholder": "Enter confirm password"})
        }

    def password_clean(self):
        data = self.cleaned_data
        if data['password1'] != data["password2"]:
            self.add_error("password2", "Confirm password does not match")
        return super().clean()        
    
    # def username_clean(self):
    #     data = self.cleaned_data
    #     data['username'] = str(data['first_name']) + str(data['last_name'])
    #     print(super().clean())
    #     return super().clean()


class UserAuthForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['email', 'password']


class UserWishList(AbstractForm):
    # user = super().get_user()
    

    class Meta:
        model = WishList
        fields = ['variant']


class Address(ModelForm):
    class Meta:
        model = Address
        fields = ['user', 'company_name', 'address', 'city', 'country']


class DiscountCode(ModelForm):
    class Meta:
        model = Discount
        fields = ['code']


class Shopcart(ModelForm):
    class Meta:
        model = ProductToBasket
        fields = ['variant']

