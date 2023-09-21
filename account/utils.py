from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import six
import requests 
import os
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from pavshop import settings

class AccountActivationTokenGeneration(PasswordResetTokenGenerator):
   def _make_hash_value(self, user: AbstractBaseUser, timestamp: int) -> str:
      return (
         six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
      )

account_activation_token = AccountActivationTokenGeneration()



