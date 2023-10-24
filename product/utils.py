from datetime import datetime


from django.db.models import Sum


from .models import Variant, Discount, DiscountType


def get_current_discount():
  return Discount.objects.filter(deleted_at=False, date_begin__gte=datetime.now(), date_end__lte=datetime.now())

'''  показать товары у которых суммарное кол-во в стоке больше чем суммарное кол-во в заказах 1, 2 
     Вычисляем кол-во variant в наличии (не оплаченные  и не зарезервированне ) во всех store  filter('quant__gt=0')'''

def count_variant():
  # quantity_to_store = Variant.objects.aggregate(quantity = Sum(''))
  return Variant.objects.annotate(quantit = Sum('varianttostore__quantity') - Sum('variantinbasket__count')).filter(quantit__gt=0)


def current_price(variant):
    current_discount = variant.discount__discounts.filter(deleted_at=False, date_begin__gte=datetime.now(), date_end__lte=datetime.now())
    discount_price = []
    if current_discount['discount_id__types'] == DiscountType.objects.get(id=1):
      
      discount_price.append(1)
    if current_discount['discount_id'] == Discount.objects.get(id=2):
      discount_price.append(1)
    if current_discount['discount_id'] == Discount.objects.get(id=3):
      discount_price.append(1)
    if current_discount['discount_id'] == Discount.objects.get(id=5):
      discount_price.append(1)
    if current_discount['discount_id'] == Discount.objects.get(id=6):
      discount_price.append(1)
    if current_discount['discount_id'] == Discount.objects.get(id=7):
      discount_price.append(1)