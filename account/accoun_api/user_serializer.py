from rest_framework.serializers import ModelSerializer


from account.models import User


class UserSerializer(ModelSerializer):
   class Meta:
      model = User
      fields = (
         'first_name',
         'last_name',
      )