from django.db import models
from django.utils import timezone

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    category_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand_id = models.IntegerField()
    collection_id = models.IntegerField()
    views_id = models.IntegerField()
    description = models.TextField()
    archive = models.BooleanField(default=False)
    style_id = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Discount(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    type_id = models.IntegerField()
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    date_begin = models.DateField()
    date_end = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class DiscountType(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class ProductReview(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)


class Store(models.Model):
    title = models.CharField(max_length=150, unique=True)


class Quantity(models.Model):
    variant_id = models.ForeignKey('Variant', on_delete=models.PROTECT)


class Variant(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True)


class VariantImage(models.Model):
    image_id = models.ForeignKey('Image', blank=True)


class Image(models.Model):
    image_url = models.CharField()


class Option(models.Model):
    variant_id = models.ForeignKey('Variant', on_delete=models.PROTECT)


class PropertyValue(models.Model):
    property_id = models.ForeignKey('Property', on_delete=models.PROTECT)


class Property(models.Model):
    title = models.CharField(max_length=50)


class Designer(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Designer')


class Style(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)


class Brand(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Brand')  


class Collection(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT)

    class Meta:
        unique_together = ['title', 'brand_id']

