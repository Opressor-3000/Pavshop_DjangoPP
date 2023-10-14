from rest_framework.serializers import ModelSerializer
from ..models import ProductToBasket, WishList, Status, Order, User, Address
from product.product_api.serializers import VariantSerializer, DiscountSerializer


class StatusSerializer(ModelSerializer):
   class Meta:
      model = Status
      fields = {
         'title'
      }


class AddressSerializer(ModelSerializer):
   class Meta:
      model = Address
      fields = {
         'company_name',
         'address',
         'city',
         'country',
      }

class WishlistSerializer(ModelSerializer):
   class Meta:
      model = WishList
      fields = {
         'variant',
      }


class OrderSerializer(ModelSerializer):
   class Meta:
      model = Order
      fields = {
         'status'
      }


class UserSerialiser(ModelSerializer):
   class Meta:
      model = User
      fields = {
         'first_name',
         'last_name',
         'email',
         'phone',
         'avatar',
         'saller',
         'bloger',
      }


class ProductToBasketSerializer(ModelSerializer):
   variant = VariantSerializer()
   order = OrderSerializer()
   discount_id = DiscountSerializer()
   class Meta:
      model = ProductToBasket
      fields = {
         'order',
         'variant',
         'count',
         'discount_id',
      }