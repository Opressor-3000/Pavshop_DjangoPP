from datetime import datetime
from typing import Any, Dict


from django import template
from django.shortcuts import render
from django.db.models import Count, Sum
from django.views.generic import ListView


from product.models import Category, Variant, Style, Product, Brand, Tag, Discount, Collection, Store
from account.models import User, Order, ProductToBasket
from blog.models import Post


register = template.Library()

'''    НУжны след ФУНКЦИИ
        1   Popular 
        2   New Arrival
        3   Discount
        4   Category
        5   Style
        6   Brands
        7   Store
'''

@register.simple_tag
def get_discount(): #  показать действующие дисконты в которых есть товары 
    discount = Discount.objects.filter(deleted_at=False)
    return discount


@register.simple_tag
def get_popular():
    global popular
    popular = Variant.objects.annotate(Count('order'))
    return popular

@register.simple_tag
def get_newarrivals():
    return Variant.objects.order_by('-created_at')[:4]


@register.simple_tag
def get_styles():
    return Style.objects.all()


@register.simple_tag
def get_brands():
    return Brand.objects.filter(product__variant__varianttostore__quantity__gt=0)


@register.simple_tag
def get_stores():
    return Store.objects.all()


@register.simple_tag
def get_top_rate():
    return popular[:3]


@register.simple_tag
def get_shopcart():
    return Variant.objects.filter()


from django import template
from product.models import Category


register = template.Library()


@register.simple_tag
def categories():
    categories = Category.objects.all()
    # categories = cat.product__category.filter(variant__varianttostore__quantity__gt=0)
    return categories

