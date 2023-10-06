from django.db.models import Count
from django import template


from product.models import Variant
from account.models import ProductToBasket

register = template.Library()

@register.simple_tag
def get_shopcarts(request):
    return Variant.objects.filter(variantinbasket__user=request.user, variantinbasket__order=1)