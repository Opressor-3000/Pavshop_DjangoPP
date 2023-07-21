from django.db import models
from django.utils import timezone

class Product(models.Model): #11
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Product')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Product_slug')
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand_id = models.ForeignKey('Brand', on_delete=models.PROTECT)
    collection_id = models.ForeignKey('Collection', on_delete=models.PROTECT)
    description = models.TextField()
    archive = models.BooleanField(default=False)
    style_id = models.ForeignKey('Style', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Category')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Category_slug')
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Discount(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Discont')
    code = models.CharField(max_length=50)
    type_id = models.ForeignKey('DiscountType', on_delete=models.CASCADE)
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    date_begin = models.DateField()
    date_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class DiscountType(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Discont')
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class ProductReview(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    text = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=3, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Store(models.Model):
    title = models.CharField(max_length=50, unique=True, default='Pavshop')
    address = models.CharField(max_length=100, unique=True)
    post = models.IntegerField(max_length=6, blank=True)
    location = models.CharField(max_length=255, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Unit(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    

class Quantity(models.Model):
    variant_id = models.ForeignKey('Variant', on_delete=models.PROTECT)
    store_id = models.ForeignKey('Store', on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=3)
    unit_id = models.ForeignKey(Unit, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Variant(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Variant')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Varian_slug')
    image_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    discont_id = models.ForeignKey(Discount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Image(models.Model):
    image_url = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


# class Option(models.Model):
#     variant_id = models.ForeignKey('Variant', on_delete=models.PROTECT)


# class PropertyValue(models.Model):
#     property_id = models.ForeignKey('Property', on_delete=models.PROTECT)


# class Property(models.Model):
#     title = models.CharField(max_length=50)


class Designer(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Designer')
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Style(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Brand(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Brand')  
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Collection(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['title', 'brand_id']

