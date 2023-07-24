from django import forms


from .models import *


class AddReview(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].empty_lable = 'Product not selected'
        # self.queryset = Post.objects.filter(name__startswith="O")

    class Meta:
        model = Post
        fields = ['title', 'text', 'preview', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class':''})
        }


