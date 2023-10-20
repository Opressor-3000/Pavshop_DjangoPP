from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ..models import *


class PostReviewSerializer(ModelSerializer):
   pass


class BlogsListSerailizer(ModelSerializer):
   review = SerializerMethodField()
   class Meta:
      model = Post
      fields = {
         'title',
         'author',
         'preview'
         'created_at',
         'review'
      }

   def get_review(self, obj):
      serializer = PostReviewSerializer(obj.post.all(), context=self.context, many=True)

class BlogsOfTagSerializer(ModelSerializer):
   blogs = SerializerMethodField()
   class Meta:
      model = Tag
      fields = {
         'blogs',
      }      

   def get_blogs(self, obj):
      serializer = BlogsListSerailizer(obj.tags.all(), context=self.context, many=True)
      return serializer.data


class BlogsOfAuthorSerializer(ModelSerializer):
   blogs = SerializerMethodField()
   class Meta:
      model = User
      fields = {
         'blogs',
      }

   def get_blogs(self, obj):
      serializer = BlogsListSerailizer(obj.author.all(), context=self.context, many=True)


class BlogsOfCategorySerializer(ModelSerializer):
   blogs = SerializerMethodField()
   class Meta:
      model = Category
      fields = {
         'blogs',
      }

   def get_blogs(self, obj):
      serializer = BlogsListSerailizer(obj.categories.all(), context=self.context, many=True)


class BlogsOfProductSerializer(ModelSerializer):
   blogs = SerializerMethodField()
   class Meta:
      model = Product
      fields = {
         'blogs',
      }

   def get_blogs(self, obj):
      serializer = BlogsListSerailizer(obj.productsofpost.all(), contaxt=self.context, many=True)
