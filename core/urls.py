from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('about_us/', about_us, name = 'about_us'),
    path('contact/', contact, name = 'contact'),
    path('index/', index, name = 'index'),

]