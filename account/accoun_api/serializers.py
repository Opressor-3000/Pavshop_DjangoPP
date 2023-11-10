from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.tokens import Token
from ..models import ProductToBasket, WishList, Status, Order, User, Address, Variant
from product.product_api.serializers import VariantSerializer, DiscountSerializer, SerializerMethodField, CollectionSerializer, ProductReviewSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from blog.blog_api.serializers import PostReviewSerializer, PostListSerializer



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
   @classmethod
   def get_token(cls, user) -> Token:
      token = super().get_token(user)
      return token


class StatusSerializer(ModelSerializer):
   class Meta:
      model = Status
      fields = (
         'title'
      )


class AddressSerializer(ModelSerializer):
   class Meta:
      model = Address
      fields = (
         'company_name',
         'address',
         'city',
         'country',
      )


class WishlistSerializer(ModelSerializer):
   class Meta:
      model = WishList
      fields = (
         'variant',
      )


class OrderSerializer(ModelSerializer):
   status=StatusSerializer()
   class Meta:
      model = Order
      fields = (
         'status',
      )


class UserSerializer(ModelSerializer):
   class Meta:
      model = User
      fields = (
         'first_name',
         'last_name',
      )


class ProductToBasketSerializer(ModelSerializer):
   class Meta:
      model = ProductToBasket
      fields = (
         'user',
         'order',
         'variant',
         'count',
         'discount_id',
      )


#---------------------------------------------------------------------------------------------------------------------------------


class StatusOrderSerializer(ModelSerializer):
   order = SerializerMethodField()
   class Meta:
      model = Status
      field = (
         'order',
         'title'
      )

   def get_order(self, obj):
      serializer = OrderSerializer(obj.status.all(), context=self.context, many=True)
      return serializer.data


class CurrentUserSerializer(ModelSerializer):
   # def get_user(self):
   #    return self.context['request'].user
   
   # user = get_user()
   class Meta:
      model = User
      fields = (
         'user',
      )


class OrdersOfUserSerializer(ModelSerializer):
   status = StatusSerializer()
   user = CurrentUserSerializer()
   producttobasket = SerializerMethodField()
   class Meta:
      model = Order
      fields = (
         'user'
         'id',
         'status',
         'producttobasket',
      )

   def get_producttobasket(self):
      serializer = ProductToBasketOrdersSerializer()
      return serializer.data
   

class ProductToBasketOrdersSerializer(ModelSerializer):
   variant = VariantSerializer()
   user = CurrentUserSerializer()
   class Meta:
      model = ProductToBasket
      fields = (
         'user',
         'order',
         'variant',
      )


class ProdictToBasketSerializer(ModelSerializer):
   order = OrderSerializer()
   variant = VariantSerializer()
   class Meta:
      model = ProductToBasket
      fields = (
         'order',
         'variant',
         'count',
      )


class UserShoppingCartSerializer(ModelSerializer):
   user = CurrentUserSerializer()
   order = SerializerMethodField()
   class Meta:
      model = User
      fields = (
         'user'
         'order',
      )

   def get_order(self):
      serializer = OrdersOfUserSerializer()
      return serializer.data
   

class UserAddressserializer(ModelSerializer):
   user = CurrentUserSerializer()
   class Meta:
      model = Address
      fields = (
         'user',
         'address',
         'company_name',
         'city',
         'country',
      )


class AddToWishListSerializer(ModelSerializer):
   variant = VariantSerializer
   class Meta:
      model = WishList
      fields = (
         'user',
         'variant'
      )


class UserAccountSerializer(ModelSerializer):
   wishlist = SerializerMethodField()
   orders = SerializerMethodField()
   address = SerializerMethodField()
   
   class Meta:
      model = User
      fields = (
         'first_name',
         'last_name',
         'wishlist',
         'orders',
         'address',
         
        
         
      )

   def get_orders(self, obj):
      serializer = OrderSerializer(obj.user_id.all(), context=self.context, many=True)

   def get_wishlist(self, obj):
      serializer = WishListSerializer(obj.wishlistuser.all(), context=self.context, many=True)

      
   # def get_address(self, obj):
   #    serializer = AddressSerializer(obj.user.all(), context=self.context, many=True)



#------------------------------------------------------------------------------------------------------------------------------------------------


