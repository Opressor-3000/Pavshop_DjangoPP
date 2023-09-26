from django.db.models import Count
from django import template


from product.models import Brand

register = template.Library()

@register.simple_tag
def get_brands():
    return Brand.objects.filter(product__variant__varianttostore__quantity__gt=0)