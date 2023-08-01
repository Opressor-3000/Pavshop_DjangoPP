from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy


from core.models import AbstractModel, Tag
from account.models import User


class Category(AbstractModel):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Category')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, parent_link='parents', related_name='parents')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Category_slug')
    
    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category':self.title})
    
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
    
    def get_absolute_url(self, **kwargs):
        return reverse_lazy('product', kwargs={'discounttype': self.title })

    
class Discount(AbstractModel):
    title = models.CharField(max_length=100, unique=True, verbose_name='Discont')
    code = models.CharField(max_length=50)
    type_id = models.ForeignKey(DiscountType, on_delete=models.PROTECT, related_name='types')
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    date_begin = models.DateField()
    date_end = models.DateField()
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('product/', kwargs={'product':self.title})

    class Meta:
        verbose_name = 'discont'
        verbose_name_plural = 'disconts'
        ordering = ['-pk']


class ProductReview(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='User', related_name='userreview')
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='productreview')
    text = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=3, blank=True)
    published_at = models.BooleanField(default=False)
  
    def __str__(self) -> str:
        return f'{self.user} {self.product}'
    
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

    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
    
    def __str__(self) -> str:
        return self.title

class Image(AbstractModel):
    image_url = models.ImageField(upload_to='product_images/', unique=True, db_index=True,)

    def __str__(self) -> str:
        return self.pk


class Color(AbstractModel):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Color')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='color_slug')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'
        ordering = ['title']


class Designer(AbstractModel):
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Designer')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Varian_slug')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('designer', kwargs={'designer':self.title})

    class Meta:
        verbose_name = 'designer'
        verbose_name_plural = 'designers'
        ordering = ['name']


class Style(AbstractModel):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Style')
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
   
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('style', kwargs={'style':self.title})

    class Meta:
        verbose_name = 'style'
        verbose_name_plural = 'styles'
        ordering = ['title']


class Brand(AbstractModel):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Brand')  
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('brand', kwargs={'brand':self.title})
    
    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
        ordering = ['title']


class Collection(AbstractModel):
    title = models.CharField(max_length=100, db_index=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('collection', kwargs={'collection':self.title})

    class Meta:
        unique_together = ['title', 'brand_id']
        verbose_name = 'collection'
        verbose_name_plural = 'collections'
        ordering = ['brand_id']


class Product(AbstractModel): #11
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Product')
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='category')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='fabric price')
    brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT, blank=True, null=True, related_name='brand')
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE, blank=True, null=True, related_name='collection')
    views = models.IntegerField(null=True, verbose_name='viewer')
    description = models.TextField(blank=True, verbose_name='Description')
    archive = models.BooleanField(default=False, verbose_name='Archived')
    style_id = models.ForeignKey(Style, on_delete=models.PROTECT, blank=True, null=True, related_name='style')
    tag = models.ManyToManyField(Tag, related_name='product_tag')

    def get_absolute_url(self):
        return reverse_lazy('product/', kwargs={'product':self.title})
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['-pk']


class Variant(AbstractModel):
    title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='variant')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='color')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Varian_slug')
    image_id = models.ManyToManyField(Image, verbose_name='Image')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True, verbose_name='price')
    discont_id = models.ManyToManyField(Discount, verbose_name='Discont')
    quantity = models.IntegerField(verbose_name='Quantity')
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True, verbose_name='Unit')
    tag = models.ManyToManyField(Tag, related_name='variant_tag')
  
    def get_absolute_url(self):
        return reverse_lazy('variant', kwargs={'product':self.title})
    
    def __str__(self) -> str:
        return f'{self.title} {self.color} {self.unit}'
    
    class Meta:
        verbose_name = 'variant'
        verbose_name_plural = 'variants'
        ordering = ['title']