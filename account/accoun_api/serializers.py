from rest_framework.serializers import ModelSerializer
from ..models import ProductToBasket, WishList, Status, Order, User, Address, Variant
from product.product_api.serializers import VariantSerializer, DiscountSerializer, SerializerMethodField, CollectionSerializer


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
         'status',
      }


class UserSerializer(ModelSerializer):
   class Meta:
      model = User
      fields = {
         'first_name',
         'last_name',
      }


#---------------------------------------------------------------------------------------------------------------------------------


class StatusOrderSerializer(ModelSerializer):
   order = SerializerMethodField()
   class Meta:
      model = Status
      field = {
         'order'
      }

   def get_order(self, obj):
      serializer = OrderSerializer(obj.status.all(), context=self.context, many=True)
      return serializer.data


class CurrentUserSerializer(ModelSerializer):
   # def get_user(self):
   #    return self.context['request'].user
   
   # user = get_user()
   class Meta:
      model = User
      fields = {
         'user',
      }


class OrdersOfUserSerializer(ModelSerializer):
   status = StatusSerializer()
   user = CurrentUserSerializer()
   producttobasket = SerializerMethodField()
   class Meta:
      model = Order
      fields = {
         'user'
         'id',

      }

   def get_producttobasket(self):
      ptb = ProductToBasketOrdersSerializer()
   

class ProductToBasketOrdersSerializer(ModelSerializer):
   variant = VariantSerializer()
   user = CurrentUserSerializer()
   class Meta:
      model = ProductToBasket
      fields = {
         'user',
         'order',
         'variant',
      }


class ProdictToBasketSerializer(ModelSerializer):
   order = OrderSerializer()
   variant = VariantSerializer()
   class Meta:
      model = ProductToBasket
      fields = {
         'order',
         'variant',
         'count',

      }


class UserShoppingCartSerializer(ModelSerializer):
   user = CurrentUserSerializer()
   order = SerializerMethodField()
   class Meta:
      model = User
      fields = {
         'user'
         'order',
      }

   def get_order(self):
      serializer = OrdersOfUserSerializer()
      return serializer.data
   

class UserAddressserializer(ModelSerializer):
   user = CurrentUserSerializer()
   class Meta:
      model = Address
      fields = {
         'user',
         'address',
         'company_name',
         'city',
         'country',
      }


class WishListSerializer(ModelSerializer):
   variant = VariantSerializer
   class Meta:
      model = WishList
      fields = {
         'variant'
      }


class UserAccountSerializer(ModelSerializer):
   wishlist = SerializerMethodField()
   orders = SerializerMethodField()
   address = SerializerMethodField()
   status = StatusOrderSerializer()
   class Meta:
      model = User
      fields = {
         'first_name',
         'last_name',
         'whislist',
         'status',
         'orders',
         'address',
      }

   def get_status(self, obj):
      serializer = StatusOrderSerializer(obj.status.all(), context=self.context, many=True)

   def get_orders(self, obj):
      serializer = OrderSerializer(obj.user_id.all(), context=self.context, many=True)

   def get_wishlist(self, obj):
      serializer = WishListSerializer(obj.wishlistuser.all(), context=self.context, many=True)

   def get_address(self, obj):
      serializer = AddressSerializer(obj.user.all(), context=self.context, many=True)



#------------------------------------------------------------------------------------------------------------------------------------------------


class SellerEditerSerializer(ModelSerializer):
   class Meta:
      model = User
      fields = {

      }