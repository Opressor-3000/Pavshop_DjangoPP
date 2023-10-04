from django import template


from product.models import Style
from core.utils import count_variant


register = template.Library()

@register.simple_tag
def get_style():
    return Style.objects.all()