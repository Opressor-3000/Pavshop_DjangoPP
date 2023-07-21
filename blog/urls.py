from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('blog_detail/<slug:postid/>', PostDetail.as_view(), name = 'blog_detail'),
    path('blog_list/', PostList.as_view(), name = 'blog_list'),

]