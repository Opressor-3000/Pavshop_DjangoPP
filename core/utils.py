from functools import wraps

from product.models import Category, Brand, Style, Collection, Variant
from account.models import Order, ProductToBasket
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


'''  показать товары у которых суммарное кол-во в стоке больше чем суммарное кол-во в заказах 1, 2 
     Вычисляем кол-во variant в наличии (не оплаченные  и не зарезервированне ) во всех store  filter('quant__gt=0')'''

def count_variant():
  return Variant.objects.annotate(quantit = Sum('varianttostore__quantity') - Sum('variant__count')).filter(quantit__gt=0)
  
