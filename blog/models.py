from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy

from account.models import User
from product.models import Image, Tag, Category, Product
from core.Abstact_models import AbstractModel


class PostReview(AbstractModel):
    post = models.ForeignKey('Post', on_delete=models.PROTECT, related_name='post')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='userrew')
    text = models.TextField(verbose_name='')
    review = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, related_name='reviewsr')
    deleted_at = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
        ordering = ['pk']

    def __str__(self) -> str:
        return f'{self.user} review {self.post} {self.review}'


class Post(AbstractModel):
    title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Title')
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Author', related_name='author')
    text = models.TextField(verbose_name='Content')
    Preview = models.ImageField(upload_to='blog_image/', verbose_name='Preview')
    image = models.ManyToManyField(Image, blank=True, verbose_name='Image')
    published_at = models.BooleanField(default=False, verbose_name='Published at')  
    tag = models.ManyToManyField(Tag, verbose_name='Tags')
    category = models.ManyToManyField(Category, blank=True ,verbose_name='About Categories')
    product = models.ManyToManyField(Product, blank=True ,verbose_name='About Products')
    deleted_at = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['created_at']
    
    def get_absolute_url(self):
        return reverse_lazy('blog_detail', kwargs={'post': self.title })
    
    def __str__(self):
        return self.title 
