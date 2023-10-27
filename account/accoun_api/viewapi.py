from rest_framework.generics import RetrieveUpdateDestroyAPIView


from account.models import *
from .serializers import UserAccountSerializer


class AccountAPIView(RetrieveUpdateDestroyAPIView):
   queryset = User
   serializer_class = UserAccountSerializer

   