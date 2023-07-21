from django import forms


from .models import *


class Contact(forms.ModelForm):
    class Meta:
        model = Contact


        