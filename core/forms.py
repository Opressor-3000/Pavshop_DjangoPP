from django.forms import ModelForm, TextInput, EmailInput, Textarea, CharField
 

from .models import *


class AbstractForm(ModelForm):
    
    def get_user(request):
        user = request.user.pk
        return user


class ContactForm(ModelForm):    
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'subject', 'message']
        widget = {
            'name' : TextInput(attrs={"type":"text", "class": "form-control", "placeholder": "Enter your name"}),
            'phone' : TextInput(attrs={"type":"text", "class": "form-control", "placeholder": "Enter your phone"}),
            'email' : EmailInput(attrs={"type":"text", "class": "form-control", "placeholder": "Enter your e-mail"}),
            'subject' : TextInput(attrs={"type":"text", "class": "form-control", "placeholder": "Enter subject"}),
            'message' : Textarea(attrs={"type":"text", "class": "form-control", "placeholder": "Enter your messsage"}),
        }


class SubscriberForm(ModelForm):

    class Meta:
        model = Subscriber
        fields = ['email']
