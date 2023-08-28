from django import forms


from .models import *


class AbstractForm(forms.ModelForm):
    
    def get_user(request):
        user = request.user.pk
        return user


class Contact(forms.ModelForm):
        
    class Meta:
        model = Contact
        fields = ['email']


class Subscriber(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ['email']