from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('blog_detail/', blog_detail, name = 'blog_detail'),
    path('blog_list/', blog_list, name = 'blog_list'),

]