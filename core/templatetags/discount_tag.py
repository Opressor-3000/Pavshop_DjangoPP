from django import template


from product.models import Variant, Discount
from core.utils import count_variant


register = template.Library()

@register.simple_tag
def get_style():
    discount = Discount.objects.all()