from django.urls import path


from .viewapi import AccountAPIView


app_name = 'account_api'


urlpatterns = [
    path('', AccountAPIView.as_view(), name='account_api'),
]