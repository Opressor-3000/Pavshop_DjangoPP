from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('<slug:postid>/', PostDetail.as_view(), name = 'blog_detail'),
    path('list/', PostList.as_view(), name = 'blog_list'),
]

