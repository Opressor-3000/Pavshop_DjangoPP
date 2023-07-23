from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy


from core.models import AbstractModel
from account.models import User


class Category(AbstractModel):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Category')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Category_slug')
    
    def get_absolute_url(self):
        return reverse_lazy('category/', kwargs={'product':self.pk})
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['title']


class DiscountType(AbstractModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Discont')
    
    def __str__(self) -> str:
        return self.pk

    
class Discount(AbstractModel):
    title = models.CharField(max_length=100, unique=True, verbose_name='Discont')
    code = models.CharField(max_length=50)
    type_id = models.ForeignKey(DiscountType, on_delete=models.PROTECT)
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    date_begin = models.DateField()
    date_end = models.DateField()
    
    def __str__(self) -> str:
        return self.pk

    class Meta:
        verbose_name = 'discont'
        verbose_name_plural = 'disconts'
        ordering = ['-pk']


class ProductReview(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    text = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=3, blank=True)
    published_at = models.BooleanField(default=False)
  
    def __str__(self) -> str:
        return self.pk
    
    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
        ordering = ['pk']


class Store(AbstractModel):
    title = models.CharField(max_length=50, unique=True, default='Pavshop')
    address = models.CharField(max_length=100, unique=True)
    post = models.IntegerField(blank=True)
    location = models.CharField(max_length=255, blank=True, unique=True)
   
    def __str__(self) -> str:
        return self.pk
    
    class Meta:
        verbose_name = 'store'
        verbose_name_plural = 'stores'
        ordering = ['title']

class Unit(AbstractModel):
    title = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.pk

class Image(AbstractModel):
    image_url = models.ImageField(upload_to='product_images/', unique=True, db_index=True,)


class Color(AbstractModel):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Color')
    

class Designer(AbstractModel):
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Designer')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Varian_slug')


    class Meta:
        verbose_name = 'designer'
        verbose_name_plural = 'designers'
        ordering = ['name']
   

class Style(AbstractModel):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Style')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Style_slug')
   
    class Meta:
        verbose_name = 'style'
        verbose_name_plural = 'styles'
        ordering = ['title']


class Brand(AbstractModel):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Brand')  
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Brand_slug')

  
    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
        ordering = ['title']


class Collection(AbstractModel):
    title = models.CharField(max_length=100, db_index=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Collection_slug')


    class Meta:
        unique_together = ['title', 'brand_id']
        verbose_name = 'collection'
        verbose_name_plural = 'collections'
        ordering = ['brand_id']


class Product(AbstractModel): #11
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Product')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Product_slug')
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='fabric price')
    brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT)
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE)
    views = models.IntegerField(null=True, verbose_name='viewer')
    description = models.TextField()
    archive = models.BooleanField(default=False, verbose_name='Archived')
    style_id = models.ForeignKey('Style', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse_lazy('product/', kwargs={'product':self.pk})
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['-pk']


class Variant(AbstractModel):
    title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Variant')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Varian_slug')
    image_id = models.ManyToManyField(Image)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True, verbose_name='price')
    discont_id = models.ManyToManyField(Discount)
    quantity = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True)
  
    def get_absolute_url(self):
        return reverse_lazy('product/', kwargs={'product':self.pk})
    
    def __str__(self) -> str:
        return self.tit
    
    class Meta:
        verbose_name = 'variant'
        verbose_name_plural = 'variants'
        ordering = ['title']