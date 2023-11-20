from django.http import HttpResponse
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


from account.models import *
from .serializers import (
    UserAccountSerializer,
    AddToWishListSerializer,
    ProductToBasketListSerializer,
    WishlistSerializer,
    ProductToBasketOldOrderSerializer,
    AddToCartOrderSerializer,
)


class AccountAPIView(RetrieveUpdateDestroyAPIView):
   queryset = User
   serializer_class = UserAccountSerializer
   authentication_classes = [SessionAuthentication, BasicAuthentication]
   permission_classes = [IsAuthenticated]
   pagination_class = LimitOffsetPagination

   def get(self, request, *args, **kwags):
      if request.user.is_authenticated:
         cart_products = ProductToBasket.objects.filter(user=request.user)
         products_list = ProductToBasketListSerializer(cart_products, many=True).data
         return Response(products_list)

   def get_serializer_context(self):
      if self.request.user.is_authenticated:
         return super().get_serializer_context()
      else:
         return HttpResponse("Unauthorized", status=401)


class AddWishlistAPIView(RetrieveUpdateDestroyAPIView):
   queryset = WishList
   serializer_class = AddToWishListSerializer
   authentication_classes = [SessionAuthentication, BasicAuthentication]
   permission_classes = [IsAuthenticated]

   def post(self, request, *args, **kwargs):
      if request.user.is_authenticated:
         variant = Variant.objects.filter(id=int(request.data["variant"])).first()
         if WishList.objects.filter(
            user=request.user, variant=variant
         ).first():
            WishList.objects.filter(
                  user=request.user, variant=request.data["variant"]
            ).delete()
         else:
            
            WishList.objects.create(user=request.user, variant=variant)

         return Response("success")



class ProductToBasketOldOrderAPIView(RetrieveUpdateDestroyAPIView):
   queryset = ProductToBasket
   serializer_class=ProductToBasketOldOrderSerializer
   authentication_classes = [SessionAuthentication, BasicAuthentication]
   permission_classes = [IsAuthenticated]

   def post(self, request, *args, **kwargs):
      if request.user.is_authenticated:
         variant = Variant.objects.filter(id=int(request.data["variant"])).first()
         if ProductToBasket.object.filter(user=request.user.id, variant=variant, order__status=1, count__gt=0).first():
            ProductToBasket.object.filter(user=request.user.id, variant=variant, order__status=1, count__gt=0).first().delete()
         else:
            ProductToBasket.object.filter(user=request.user.id, variant=variant, order__status=1, count__gt=0).create()
         return Response('Product successful deleted')

   def delete(self, request, *args, **kwargs):
      if request.user.is_authenticated:
         variant = Variant.objects.filter(id=int(request.data["variant"])).first()
         if ProductToBasket.object.filter(user=request.user.id, variant=variant, order__status=1, count__gt=0).first():
            ProductToBasket.object.filter(user=request.user.id, variant=variant, order__status=1, count__gt=0).first().delete()
         else:
            ProductToBasket.object.filter(user=request.user.id, variant=variant, order__status=1, count__gt=0).create()
         return Response('Product successful deleted')
   
   def perform_destroy(self, instance):
      return super().perform_destroy(instance)
   
   def update(self, request, *args, **kwargs):
      
      return super().update(request, *args, **kwargs)
   

class ShoppingCartAPIView(RetrieveUpdateDestroyAPIView):
   queryset = ProductToBasket
   serializer_class = ProductToBasketListSerializer
   authentication_classes = [SessionAuthentication, BasicAuthentication]
   permission_classes = [IsAuthenticated]

   def get(self, request, *args, **kwargs):
      if request.user.is_authenticated:
         order = Order.objects.filter(user=request.user.id, status=1).first()
         shopcart = ProductToBasket.objects.filter(order=order, user=request.user.id)
         result = ProductToBasketListSerializer(shopcart, many=True).data
         return Response(result)
   

class WishlistAPIView(RetrieveUpdateDestroyAPIView):
   queryset = WishList
   serializer_class = WishlistSerializer
   authentication_classes = [SessionAuthentication, BasicAuthentication]
   permission_classes = [IsAuthenticated] 

   def get(self, request, *args, **kwags):
      if request.user.is_authenticated:
         user = WishList.objects.filter(user=request.user.id)
         wishlist = WishlistSerializer(user, many=True).data
         return Response(wishlist)


class AddToCartAPIView(RetrieveUpdateDestroyAPIView):
   queryset = ProductToBasket
   serializer_class = AddToCartOrderSerializer
   authentication_classes = [SessionAuthentication, BasicAuthentication]
   permission_classes = [IsAuthenticated] 

   def get(self, request, *args, **kwags):
      if request.user.is_authenticated:
         user = Order.objects.filter(user=request.user.id).filter(status=1).first()
         product = ProductToBasket.objects.filter(order=user, user=request.user.id).first()
         addtocart = AddToCartOrderSerializer(product).data
         return Response(addtocart)
      
   def addtocart(self, request, *args, **kwargs):
      if request.user.is_authenticated:
         if ProductToBasket.objects.filter(
               user=request.user, order=request.data["variant"], variant=request.data["variant"]
            ).first():
               WishList.objects.filter(
                     user=request.user, variant=request.data["variant"]
               ).delete()
         else:
            variant = Variant.objects.filter(id=int(request.data["variant"])).first()
            WishList.objects.create(user=request.user, variant=variant)
      
   def post(self, request, *args, **kwargs):
      if request.user.is_authenticated:
         if Order.objects.filter(user=request.user, status=1):
            order = Order.objects.filter(user=int(request.user, status=1))
            variant = Variant.objects.filter(id=request.data["variant"]).first()
            if ProductToBasket.objects.filter(
               user=request.user, order=order, variant=variant
               ).first():
               return Response("success")
            else:
               ProductToBasket.objects.create(user=request.user, order=order, variant=variant)
               return Response("success added")
         else:
            Order.objects.create(user=request.user, status=1)
            order = Order.objects.filter(user=int(request.user, status=1))
            variant = Variant.objects.filter(id=request.data["variant"]).first()
            ProductToBasket.objects.create(user=request.user, order=order, variant=variant)
               

class OrdersAPIView(ListAPIView):
   queryset = ProductToBasket
   serializer_class = ProductToBasketListSerializer
   authentication_classes = [SessionAuthentication, BasicAuthentication]
   permission_classes = [IsAuthenticated]

   def get(self, request, *args, **kwargs):
      if request.user.is_authenticated:
         status = [2, 3, 4, 5, 6, 7, 8, 9]
         order = Order.objects.filter(user=request.user.id, status__id__in=status)
         shopcart = ProductToBasket.objects.filter(order__id__in=order, user=request.user.id)
         result = ProductToBasketListSerializer(shopcart, many=True).data
         return Response(result)