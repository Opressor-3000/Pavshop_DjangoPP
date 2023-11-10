from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ..models import *
from product.product_api.serializers import CategorySerializer, TagSerializer, ProductSerializer
from account.accoun_api.user_serializer import UserSerializer


class PostReviewSerializer(ModelSerializer):
   class Meta:
      model = PostReview
      fields = {
         'user',
         'text',
         'review',
         'created_at',
      }


class PostListSerializer(ModelSerializer):
   class Meta:
      model = Post
      fields = {
         'title',
         'author',
         'preview',
         'created_at'
      }


class Postserializer(ModelSerializer):
   category = CategorySerializer()
   tag = TagSerializer()
   product = ProductSerializer()
   author = UserSerializer()
   class Meta:
      model = Post
      fields = {
         'title',
         'author',
         'preview',
         'text',
         'image',
         'created_at',
         'tag',
         'category',
         'product',

      }


class BlogsListSerailizer(ModelSerializer):
   review = SerializerMethodField()
   class Meta:
      model = Post
      fields = {
         'review',
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



class BlogListSerializer(ModelSerializer):
   blogproduct = BlogsOfProductSerializer()
   blogauthor = BlogsOfAuthorSerializer()
   blogtag = BlogsOfTagSerializer()
   blogcategory = BlogsOfCategorySerializer()
   class Meta:
      model = Post
      fields = {
         'blogproduct',
         'blogcategory',
         'blogauthor',
         'blogtag',
      }

   def get_blogproduct(self, obj):
      serializer = BlogsOfProductSerializer(obj.productofpost.all(), context=self.context, many=True)
      return serializer.data
   
   def get_blogauthor(self, obj):
      serializer = BlogsOfAuthorSerializer(obj.author.all(), context=self.context, many=True)
      return serializer.data
   
   def get_blogtag(self, obj):
      serializer = BlogsOfTagSerializer(obj.tags.all(), context=self.context, many=True)
      return serializer.data
   
   def get_blogcategory(self, obj):
      serializer = BlogsOfCategorySerializer(obj.categories.all(), context=self.context, many=True)
      return serializer.data

