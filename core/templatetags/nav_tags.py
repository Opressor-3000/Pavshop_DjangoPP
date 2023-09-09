# from datetime import datetime
# from typing import Any, Dict


# from django import template
# from django.shortcuts import render
# from django.db.models import Count, Sum
# from django.views.generic import ListView


# from product.models import Category, Variant, Style, Product, Brand, Tag, Discount, Collection
# from account.models import User, Order, ProductToBasket
# from blog.models import Post


# register = template.Library()


# def get_categories(requset):
#     cat = Category.objects.all()
#     return cat


# @register.inclusion_tag('core/base.html')
# def show_navbar(arg1=None):
#     cat = Category.objects.filter()[:10]
#     brand = Brand.objects.all()[:10]
#     collection = Collection.objects.all()[:10]
#     style = Style.objects.all()
#     blog = Post.objects.filter(delete_at=False).order_by('-created_at')
#     shopcart = 1

# # class Shopcartlist(ListView):
# #     model = ProductToBasket
# #     template_name = 'account/shopping_cart.html.html'
# #     context_object_name = 'shopcartlist'
# #     slug_url_kwarg = 'user_pk'

# #     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
# #         context = super().get_context_data(**kwargs)



# def shopcart(request):
#     shopcartlist = ProductToBasket.objects.filter(order=1).filter(user=request.user)
#     return render(request, 'shopcart', {'shopcartlist':shopcartlist})


# @register.simple_tag
# def get_user():
#     pass


# @register.simple_tag
# def get_brands():
#     brands = Brand.objects.filter(product__variant__varianttostore__quantity__gte = 1).order_by('title')
#     return brands


# @register.simple_tag
# def get_collection():
#     pass

# @register.simple_tag
# def get_style():
#     styles = Style.objects.all().order_by('title').count(Product)
#     return styles


# @register.simple_tag
# def get_new():
#     new_arrival = Variant.objects.filter(varianttostore__quantity__gte = 1).order_by('created_at')[:12]
#     return new_arrival


# @register.simple_tag
# def get_populat():
#     popular = Variant.objects.annotate(pop = Sum('producttobasket__count'))[:5]
#     return popular
    

# @register.simple_tag
# def get_tag_list():
#     tag = Tag.objects.annotate(count = Count('variant'))
#     tag_list = tag.order_by('count')
#     return tag_list
    

# @register.simple_tag
# def get_discount(): #  показать действующие дисконты в которых есть товары 
#     discount = Discount.objects.filter(date_begin__gt=datetime.now()).filter(date_end__lt=datetime.now).filter(deleted_at=False).filter(variant__in_stock=True).order_by('-date_begin')
#     return discount

from django import template
from product.models import Category

register = template.Library()

@register.simple_tag
def Nav():
    categories = Category.objects.all().order_by('created_at')
    return categories
