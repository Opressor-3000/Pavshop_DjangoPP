from django import forms


from .models import *


class AddReview(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']


