from django.db.models import Count
from django import template


from product.models import Variant
from account.models import ProductToBasket

register = template.Library()

@register.simple_tag
def get_shopcarts(request):
    return Variant.objects.filter(variant__user=request.user, variant__order=1)

