from django.db.models import Sum, F
from django import template
from .get_shopcart import get_shopcarts


register = template.Library()


@register.simple_tag
def get_subtotal(request):
   subtotal = get_shopcarts(request).aggregate(Sum('price'))
   return subtotal.get('price__sum')