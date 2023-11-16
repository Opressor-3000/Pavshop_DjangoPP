from django.forms import ModelForm, TextInput, EmailInput, Textarea, CharField
 

from .models import *


class AbstractForm(ModelForm):
    
    def get_user(request):
        user = request.user.pk
        return user


class ContactForm(ModelForm):
    # name = CharField(label=('Your Name'), widget=TextInput(attrs={"class": "form-control"}))
    # phone = CharField(label=('Your Phone'), widget=TextInput(attrs={"class": "form-control", "placeholder": "Enter your phone"}))
    # email = EmailField(label=('Your E-mail'), widget=EmailInput(attrs={"class": "form-control", "placeholder": "Enter your e-mail"}))
    # subject = CharField(label=('Subject'), widget=TextInput(attrs={"class": "form-control", "placeholder": "Enter subject"}))
    # message = CharField(label=('Your message'), widget=Textarea(attrs={"class": "form-control", "placeholder": "Enter your messsage"}))
    # type="text" class="form-control" name="name" id="name" placeholder=""
    
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'subject', 'message']
        widget = {
            'name' : TextInput(attrs={"class": "form-control", "placeholder": "Enter your name"}),
            'phone' : TextInput(attrs={"class": "form-control", "placeholder": "Enter your phone"}),
            'email' : EmailInput(attrs={"class": "form-control", "placeholder": "Enter your e-mail"}),
            'subject' : TextInput(attrs={"class": "form-control", "placeholder": "Enter subject"}),
            'message' : Textarea(attrs={"class": "form-control", "placeholder": "Enter your messsage"}),
        }


class SubscriberForm(ModelForm):

    class Meta:
        model = Subscriber
        fields = ['email']
