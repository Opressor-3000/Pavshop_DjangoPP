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
   

class UserSerializer(ModelSerializer):
   class Meta:
      model = User
      fields = (
         'id',
         'first_name',
         'last_name',
         'email',
         'phone'
      )


class StatusSerializer(ModelSerializer):
   class Meta:
      model = Status
      fields = (
         'title',
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
   variant = VariantSerializer()
   class Meta:
      model = WishList
      fields = (
         'variant',
      )


class ProductInOrdersSerializer(ModelSerializer):
   status=StatusSerializer()
   producttobasket = SerializerMethodField()
   class Meta:
      model = Order
      fields = (
         'id',
         'status',
         'producttobasket',
      )

   def get_producttobasket(self, obj):
      serializer = ProductToBasketOldOrderSerializer(obj.order.all(), context=self.context, many=True)


class OrderSerialiser(ModelSerializer):
   status = StatusSerializer
   class Meta:
      model = Order
      fields = (
         'id',
         'status',
      )


class ProductToBasketOldOrderSerializer(ModelSerializer):
   variant = VariantSerializer
   class Meta:
      model = ProductToBasket
      fields = {
         'variant',
         'count',

      }


class ProductToBasketListSerializer(ModelSerializer):
   order = OrderSerialiser()
   variant = VariantSerializer()
   discount_id = DiscountSerializer()
   class Meta:
      model = ProductToBasket()
      fields = (
         'order',
         'variant',
         'count',
         'discount_id',
      )


class ProductToBasketSerializer(ModelSerializer):
   order =ProductInOrdersSerializer()
   variant = VariantSerializer()
   class Meta:
      model = ProductToBasket()
      fields = (
         'order',
         'variant',
         'count',
         'discount_id',
      )


class AddToCartOrderSerializer(ModelSerializer):
   order = OrderSerialiser()
   variant = VariantSerializer()
   class Meta:
      model = ProductToBasket
      fields = (
         'user',
         'order',
         'variant',
         'count',
      )

#---------------------------------------------------------------------------------------------------------------------------------



class CurrentUserSerializer(ModelSerializer):
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

   

class UserAddressSerializer(ModelSerializer):
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
         'variant',
      )


class UserAccountSerializer(ModelSerializer):
   wishlist = SerializerMethodField()
   userorder = SerializerMethodField()
   address = SerializerMethodField()
   blogpost = SerializerMethodField()
   productreview = SerializerMethodField()
   blogreview = SerializerMethodField()
   
   
   class Meta:
      model = User
      fields = (
         'first_name',
         'last_name',
         'wishlist',
         'userorder',
         'address',
         'blogpost',
         'productreview',
         'blogreview',
      )

   def get_userorder(self, obj):
      serializer = ProductInOrdersSerializer(obj.user_id.all(), context=self.context, many=True)

   def get_wishlist(self, obj):
      serializer = WishlistSerializer(obj.wishlistuser.all(), context=self.context, many=True)
      
   def get_address(self, obj):
      serializer = AddressSerializer(obj.user.all(), context=self.context, many=True)

   def get_blogpost(self, obj):
      serializer = PostListSerializer(obj.user.all(), context=self.context, many=True)

   def get_productreview(self, obj):
      serializer = ProductReviewSerializer(obj.userreview.all(), context=self.context, many=True)

   def get_blogreview(self, obj):
      serializer = PostReviewSerializer(obj.userrew.all(), context=self.context, many=True)



#------------------------------------------------------------------------------------------------------------------------------------------------


