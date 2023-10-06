from django import template


from product.models import Discount
from product.utils import get_current_discount


register = template.Library()

@register.simple_tag
def get_style():
    return get_current_discount[:3]