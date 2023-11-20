from datetime import datetime


from django.shortcuts import render, redirect
from typing import Any, Dict
from django.db import models
from django.views.generic import ListView, CreateView
from django.db.models.query import QuerySet



from product.utils import count_variant
from blog.models import Post
from product.models import Variant, Discount, Image, Designer
from .models import *
from .forms import ContactForm


def about_us(request):
    return render(request, "core/about-us.html")

 
class Contact(CreateView):
    form_class = ContactForm
    template_name = 'core/contact.html'

    def get_success_url(self, **kwargs) -> str:
        #, kwargs={'contact_success': "your message has been sent successfully"}
        return reverse_lazy('core:homepage')

class HomePage(ListView):
    paginate_by = 9
    model = Variant
    template_name = 'core/index.html'
    context_object_name = 'newarr'
    allow_empty = True
    count_variants = count_variant()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        discount = Discount.objects.filter(deleted_at=False, date_begin__gte=datetime.now(), date_end__lte=datetime.now())
        if discount:
            context['discount_prod'] = self.count_variants.order_by('-created_at')[:2]
        else:
            context['discount_prod'] = self.count_variants.order_by('-created_at')[:2]
        context['new_arrival'] = self.count_variants.order_by('-created_at')
        context['popular_prod'] = Variant.objects.all()[:5]
        context['last_posts'] = Post.objects.all().order_by('-created_at')[:2]
        context['designer'] = Designer.objects.order_by('-created_at')[:1]
        return context
        
    
    def get_queryset(self) -> QuerySet[Any]:    
        return self.count_variants
    
    # def get_main_image(self):
    #     return Image.objects.filter(variant = self, is_main = True)

