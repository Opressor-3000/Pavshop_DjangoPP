from datetime import datetime


from django.shortcuts import render, redirect
from typing import Any, Dict
from django.db import models
from django.views.generic import ListView, CreateView
from django.db.models.query import QuerySet



from product.utils import count_variant
from product.models import Variant, Discount, Image
from .models import *


def about_us(request):
    return render(request, "core/about-us.html")


class Contact(CreateView):
    model = Contact
    template_name = 'core/contact.html'

# def contact(request):
#     return render("contact.html")


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
            context['discount_prod'] = self.count_variants.filter(discount_id__in=discount)[:3]
        else:
            context['discount_prod'] = self.count_variants.order_by('-created_at')[:3]
        context['new_arrival'] = self.count_variants.order_by('-created_at')

        context['popular_prod'] = self.count_variants
        return context
        
    
    def get_queryset(self) -> QuerySet[Any]:    
        return self.count_variants.filter(varianttostore__quantity__gte=1).order_by('-created_at')[:8]
    
    def get_main_image(self):
        return Image.objects.filter(variant = self, is_main = True)
    


def add_wishlist(requset):
    pass
#     pid = requset.GET['newarr']
#     variant = Variant.objects.get(pk=pid.id)
#     data = {}
#     if WishList.object.filter(user=requset.user, variant=variant):
#         data={
#             "bool": False
#         }
#     else:
#         WishList.objects.create(
#             user=requset.GET.get['user']
#             variant=variant
#         )
#         data={
#             "bool": True
#         }
#         return JsonResponse(data)


