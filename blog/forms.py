from django.forms import Textarea, TextInput, ModelForm

from .models import *
from core.forms import AbstractForm


class AddReview(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].empty_lable = 'Product not selected'
        # self.queryset = Post.objects.filter(name__startswith="O")

    class Meta:
        model = Post
        fields = ['title', 'text', 'preview', 'image']
        widgets = {
            'title': TextInput(attrs={'class':''})
        }


class PostReviewForm(AbstractForm):
   class Meta:
       model = PostReview
       fields = [
                 'text',
                 ]
       widget = {
           'text':Textarea(attrs={"class":"row"})
       }
