from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError



from account.models import *
from .serializers import UserAccountSerializer


class AccountAPIView(RetrieveUpdateDestroyAPIView):
   queryset = User
   serializer_class = UserAccountSerializer


