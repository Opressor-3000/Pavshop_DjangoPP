from functools import wraps
from datetime import datetime

from product.models import Variant, Discount
from account.models import Order
from django.db.models import Count, Sum, Q

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
  
  
