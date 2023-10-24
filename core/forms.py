from django.forms import ModelForm, TextInput
 

from .models import *


class AbstractForm(ModelForm):
    
    def get_user(request):
        user = request.user.pk
        return user


class Contact(ModelForm):
        
    class Meta:
        model = Contact
        fields = ['email']


class Subscriber(ModelForm):

    class Meta:
        model = Subscriber
        fields = ['email']
