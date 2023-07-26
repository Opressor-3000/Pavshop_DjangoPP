from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy

from account.models import User
from product.models import Product
from core.models import AbstractModel


class Image(AbstractModel):
    image = models.ImageField(upload_to='blog_image/', verbose_name='Image')
    

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['pk']

    def __str__(self) -> str:
        return f'{self.title} {self.author}'

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={'post':f'{self.title}{self.author}'})


# class Image(AbstractModel):
#     post = models.ForeignKey('Post', on_delete=models.PROTECT)
#     image = models.ForeignKey(PostImage, on_delete=models.PROTECT)

#     class Meta:
#         unique_together = ['post', 'image']


class PostReview(AbstractModel):
    post = models.ForeignKey('Post', on_delete=models.PROTECT, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.TextField(verbose_name='')
    review = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
        ordering = ['pk']


class Post(AbstractModel):
    title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Title')
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Author')
    text = models.TextField(verbose_name='Content')
    Preview = models.ImageField(upload_to='blog_image/', verbose_name='Preview')
    image = models.ManyToManyField(Image, verbose_name='Image')
    published_at = models.BooleanField(default=False, verbose_name='Published at')  