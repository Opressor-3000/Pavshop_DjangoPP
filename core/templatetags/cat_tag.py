from datetime import datetime
from typing import Any, Dict


from django import template
from django.shortcuts import render


from product.models import Category, Variant, Discount


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
def variant_in_current_order(user):
    return Variant.object.filter(producttobasket__user__id=user, producttobasket__order__status__id=1)


from django import template
from product.models import Category


register = template.Library()


@register.simple_tag
def categories():
    return Category.objects.all()




