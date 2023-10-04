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
  
def get_discount():
  Discount.objects.filter(deleted_at=False, date_begin__gte=datetime.now(), date_end__lte=datetime.now())

'''  показать товары у которых суммарное кол-во в стоке больше чем суммарное кол-во в заказах 1, 2 
     Вычисляем кол-во variant в наличии (не оплаченные  и не зарезервированне ) во всех store  filter('quant__gt=0')'''

def count_variant():
  return Variant.objects.annotate(quantit = Sum('varianttostore__quantity') - Sum('variantinptb__count')).filter(quantit__gt=0)
  
