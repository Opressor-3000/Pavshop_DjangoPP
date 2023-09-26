from django.db.models import Count
from django import template


from product.models import Variant

register = template.Library()

@register.simple_tag
def get_top_rate():
    return Variant.objects.annotate(Count('order'))[:3]