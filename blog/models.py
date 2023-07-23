from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy

from account.models import User
from product.models import Product
from core.models import AbstractModel


class PostImage(AbstractModel):
    blog_id = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='blog_image/')
    


class Post(AbstractModel):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    text = models.TextField()
    Preview = models.ImageField(upload_to='blog_image/')
    image_id = models.ForeignKey(PostImage, on_delete=models.CASCADE)
    published_at = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['pk']


    def get_absolute_url(self):
        return reverse_lazy('blog_detail', kwargs={'blog':self.pk})

    

class PostReview(AbstractModel):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, blank=True)
    review = models.TextField()
    review_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'postreview'
        verbose_name_plural = 'reviews of posts'
        ordering = ['pk']