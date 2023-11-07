from django.urls import path
from .viewapi import VariantFilterAPIView


urlpatterns = [
   path('variants/', VariantFilterAPIView.as_view(), name='list_api'),
]