from django import template
from django.db.models import Count, Sum

from product.models import Category, Variant, Style, Product, VariantToStore, Brand, Tag
from account.models import User, Order, ProductToBasket


register = template.Library()


@register.simple_tag
def get_user(request):
    user = request.user


@register.simple_tag
def get_categories(request):

    return


@register.simple_tag
def get_brands():
    brands = Brand.objects.filter(product__variant__varianttostore__quantity__gte = 1).order_by('title')
    return brands


@register.simple_tag
def get_style():
    styles = Style.objects.all().order_by('title').count(Product)
    return styles


@register.simple_tag
def get_new():
    new_arrival = Variant.objects.filter(varianttostore__quantity__gte = 1).order_by('created_at')[:12]
    return new_arrival


@register.simple_tag
def get_populat():
    popular = Variant.objects.annotate(pop = Sum('producttobasket__count'))[:5]
    return popular
    

@register.simple_tag
def get_tag_list():
    tag = Tag.objects.annotate(count = Count('variant'))
    tag_list = tag.order_by('count')
    return tag_list
    

@register.simple_tag
def get_discount():
    pass

