from django.db.models import Sum
from django import template


from product.models import Variant

register = template.Library()

@register.simple_tag
def get_top_rate():
    return Variant.objects.annotate(sum = Sum('variantinbasket')).order_by('sum')[:3]