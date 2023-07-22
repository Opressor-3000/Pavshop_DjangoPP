from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy
from core.models import AbstractModel
from account.models import User


class Product(AbstractModel): #11
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Product')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Product_slug')
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand_id = models.IntegerField()
    collection_id = models.IntegerField()
    views_id = models.IntegerField()
    description = models.TextField()
    archive = models.BooleanField(default=False)
    style_id = models.ForeignKey('Style', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse_lazy('product/', kwargs={'product':self.pk})
    
    def __str__(self) -> str:
        return self.title


class Category(AbstractModel):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Category')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Category_slug')
    
    def get_absolute_url(self):
        return reverse_lazy('category/', kwargs={'product':self.pk})
    
    def __str__(self) -> str:
        return self.title

    
class Discount(AbstractModel):
    title = models.CharField(max_length=100, unique=True, verbose_name='Discont')
    code = models.CharField(max_length=50)
    type_id = models.IntegerField()
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    date_begin = models.DateField()
    date_end = models.DateField()
    
    def __str__(self) -> str:
        return self.pk


class DiscountType(AbstractModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Discont')
    
    def __str__(self) -> str:
        return self.pk


class ProductReview(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    text = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=3, blank=True)
  
    def __str__(self) -> str:
        return self.pk


class Store(AbstractModel):
    title = models.CharField(max_length=50, unique=True, default='Pavshop')
    address = models.CharField(max_length=100, unique=True)
    post = models.IntegerField(blank=True)
    location = models.CharField(max_length=255, blank=True, unique=True)
   
    def __str__(self) -> str:
        return self.pk

class Unit(AbstractModel):
    title = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.pk


class Color(AbstractModel):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Color')


class Variant(AbstractModel):
    title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Variant')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Varian_slug')
    image_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    discont_id = models.ManyToManyField(Discount)
    quantity = models.IntegerField()
  
    def get_absolute_url(self):
        return reverse_lazy('product/', kwargs={'product':self.pk})
    
    def __str__(self) -> str:
        return self.title


class Image(AbstractModel):
    image_url = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Image')
    

class Designer(AbstractModel):
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Designer')
   

class Style(AbstractModel):
    title = models.CharField(max_length=50, unique=True, db_index=True)
   

class Brand(AbstractModel):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Brand')  
  

class Collection(AbstractModel):
    title = models.CharField(max_length=100, db_index=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT)

    class Meta:
        unique_together = ['title', 'brand_id']

