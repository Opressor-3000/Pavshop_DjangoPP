from functools import wraps

from product.models import Category, Brand, Style, Collection, Variant
from account.models import Order
from core.templatetags.nav_tags import get_shopcart

class BaseMixin:
  def get_mainmenu_context(self, **kwargs):
    pass

class CustomMixin:
  def except_variants(func):
    @wraps(func)
    def inner(*args, **kwargs):
      order_is_processed = Order.objects.filter(user=kwargs['user'], status=1)
      return func(*args, **kwargs)
    
    
    return inner

  def discount_price(func):
    @wraps
    def inner(*args, **kwargs):
      pass