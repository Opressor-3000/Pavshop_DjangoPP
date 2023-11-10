from django.urls import path
from .views import *
from core import views

app_name = 'core'

urlpatterns = [
    path('about_us/', views.about_us, name = 'about_us'),
    path('contact/', Contact.as_view(), name = 'contact'),
    path('', HomePage.as_view(), name = 'homepage'),
]