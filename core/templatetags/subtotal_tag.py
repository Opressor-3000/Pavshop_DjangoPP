from django.db.models import Sum, F
from django import template
from .shopcart_tags import get_shopcarts


from product.models import Variant
from account.models import ProductToBasket

register = template.Library()

@register.simple_tag
def get_subtotal(request):
   ptb = ProductToBasket.objects.filter(user=request.user).filter(order=1)
   return get_shopcarts(request).annotate(price=Sum('price'))

