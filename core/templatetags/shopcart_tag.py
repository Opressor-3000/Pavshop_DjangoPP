from django.db.models import Count
from django import template


from product.models import Variant

register = template.Library()

@register.simple_tag
def get_shopcart(user):
    variant = Variant.objects.filter(varianttostore__quantity__gt=0)
    return variant.producttobasket__variant.filter(user=user, status=1)

