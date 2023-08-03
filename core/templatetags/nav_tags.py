from django import template
from product.models import Category, Product, Style

register = template.Library()

@register.simple_tag
def get_categories():
    categories = Category.objects.all().order_by('title').count()
    return categories

@register.simple_tag
def get_brands():
    brands = Category.objects.all().order_by('title').count()
    return brands

@register.simple_tag
def get_style():
    styles = Style.objects.all().order_by('title').count()
    return styles

@register.simple_tag
def get_new():
    pass

@register.simple_tag
def get_populat():
    pass

@register.simple_tag
def get_tag_list():
    pass

@register.simple_tag
def get_discount():
    pass

