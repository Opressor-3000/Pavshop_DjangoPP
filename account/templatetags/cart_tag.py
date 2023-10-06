from django import template

from core.templatetags.shopcart_tags import get_shopcarts
from product.models import Product



register = template.Library()

@register.simple_tag
def get_product_detail(variant):
   return Product.objects.get(variantofproduct=variant)
