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
def get_styles():
    return Style.objects.all()


@register.simple_tag
def get_stores():
    return Store.objects.all()


# @register.simple_tag
# def get_shopcart1(user):
#     variant = Variant.objects.filter(varianttostore__quantity__gt=0)
#     return variant.producttobasket__variant.filter(user=user, status=1)


@register.simple_tag
def variant_in_current_order(user):
    variantstobasket = Variant.object.filter(producttobasket__user__id=user, producttobasket__order__status__id=1)
    return variantstobasket


from django import template
from product.models import Category


register = template.Library()


@register.simple_tag
def categories():
    categories = Category.objects.all()
    # categories = cat.product__category.filter(variant__varianttostore__quantity__gt=0)
    return categories

def current_price(variant):
    current_discount = variant.discount__discounts.filter(deleted_at=False, date_begin__gte=datetime.now(), date_end__lte=datetime.now())
    if current_discount['discount_id'] == Discount.objects.get(id=1):
        return variant
    if current_discount['discount_id'] == Discount.objects.get(id=2):
        pass
    if current_discount['discount_id'] == Discount.objects.get(id=3):
        pass
    if current_discount['discount_id'] == Discount.objects.get(id=1):
        pass



