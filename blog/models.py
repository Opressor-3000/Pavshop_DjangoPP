from django.db import models
from django.utils import timezone


from account.models import User
from product.models import Product


class PostImage(models.Model):
    blog_id = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='blog_image')
    
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    text = models.TextField()
    Preview = models.ImageField(upload_to='/blog_image/%t')
    image_id = models.ForeignKey(PostImage, on_delete=models.CASCADE)
    published_at = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class PostReview(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.PROTECT)
    review = models.TextField()
    review_id = models.ForeignKey('self', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


