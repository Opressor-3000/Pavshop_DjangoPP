from django.forms import TextInput, ModelForm, CharField, PasswordInput, EmailInput, EmailField, Textarea
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordResetForm,SetPasswordForm


from .models import *
from product.models import Discount, ProductReview
from core.forms import AbstractForm


class RegisterForm(UserCreationForm):
    first_name = CharField(label='First Name', widget=TextInput(attrs={"class": "col-md-6", "placeholder": "Enter first name"}))
    last_name = CharField(label='Last Name', widget=TextInput(attrs={"class": "col-md-6", "placeholder": "Enter last nema"}))
    phone = CharField(label='Your Phone', widget=TextInput(attrs={"class": "col-md-6", "placeholder": "Enter your phone"}))
    email = EmailField(label='Your E-mail', widget=EmailInput(attrs={"class": "col-md-6", "placeholder": "Enter your e-mail"}))
    password1 = CharField(
        label=("Password"),
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "new-password"})
    )
    password2 = CharField(
        label=("Password confirmation"),
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    def is_valid(self) -> bool:
        return super().is_valid()


    class Meta:
        # attrs={"class": "col-md-6", "placeholder": "Enter confirm password"}
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone']
        widget = {
            'first_name':TextInput(attrs={"class": "col-md-6", "placeholder": "Enter first name"}),
            'last_name':TextInput(attrs={"class": "col-md-6", "placeholder": "Enter last name"}),
            'phone':TextInput(attrs={"class": "col-md-6", "placeholder": "Enter your phone"}),
            'email':TextInput(attrs={"class": "col-md-6", "placeholder": "Enter your e-mail"})
        }


class UserAuthForm(AuthenticationForm):
    username = EmailField(widget=TextInput(attrs={
        'name': 'email',
        'class': 'col-md-12',
        'placeholder': 'email'
    }))
    password = CharField(widget=PasswordInput(attrs={
        'name': 'password',
        'class': 'col-md-12',
        'placeholder': 'password'
    }))

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


class ProductReviewForm(AbstractForm):
   class Meta:
       model = ProductReview
       fields = [
                 'text',
                 ]
       widget = {
           'text':Textarea(attrs={"class":"row"})
       }


class DiscountCode(ModelForm):
    class Meta:
        model = Discount
        fields = ['code']


class CreateOrder(ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'status']


class Shopcart(ModelForm):
    class Meta:
        model = ProductToBasket
        fields = ['variant']


class AddToCartForm(ModelForm):
    class Meta:
        model = ProductToBasket
        fields = ['variant', 'count']


class RemoveToCart(ModelForm):
    class Meta:
        model = ProductToBasket
        fields = []


class UserPasswordResetForm(PasswordResetForm):
    
     email = EmailField(
        
        max_length=254,
        widget=EmailInput(attrs={'autocomplete': 'email','class': 'form-control',"placeholder": "Email",}),
    )
class UserPasswordResetConfirmForm(SetPasswordForm):
    
     new_password1 = CharField(
        label=("New password"),
        widget = PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control',"placeholder": "New Password",}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
     new_password2 = CharField(
        label=("New password confirmation"),
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control',"placeholder": "Confirm Password",}),
    )