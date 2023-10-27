from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView


from blog.models import Post
from .serializers import BlogListSerializer


class PostListAPIView(ListAPIView):
   queryset = Post
   serializer_class = BlogListSerializer

   

