from django.urls import path


from .views_api import PostListAPIView


app_name = 'blog_api'


urlpatterns = [
    path('', PostListAPIView.as_view(), name='post_list_api'),
]