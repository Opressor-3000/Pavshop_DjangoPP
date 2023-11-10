from django.http import HttpResponse
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


from account.models import *
from .serializers import UserAccountSerializer, ProdictToBasketSerializer, AddToWishListSerializer


class AccountAPIView(RetrieveUpdateDestroyAPIView):
   queryset = User
   serializer_class = UserAccountSerializer
   authentication_classes = [SessionAuthentication, BasicAuthentication]
   permission_classes = [IsAuthenticated]
   pagination_class = LimitOffsetPagination

   def get(self, request, *args, **kwags):
      if request.user.is_authenticated:
         cart_products = ProductToBasket.objects.filter(user=request.user)
         products_list = ProdictToBasketSerializer(cart_products, many = True).data
         return Response(products_list)
   
   def get_serializer_context(self):
      if self.request.user.is_authenticated:
         return super().get_serializer_context()
      else:
         return HttpResponse('Unauthorized', status=401)


class AddWishlistAPIView(RetrieveUpdateDestroyAPIView):
   queryset = WishList
   serializer_class = AddToWishListSerializer
   
   def post(self, request, *args, **kwargs):
      print()
      if WishList.objects.filter(user=request.user, variant=request.data["variant"]).first():
         WishList.objects.filter(user=request.user,variant=request.data["variant"]).delete()
      else:
         variant=Variant.objects.filter(id=int(request.data["variant"])).first()
         WishList.objects.create(user=request.user,variant=variant)


      return Response('success')
      
