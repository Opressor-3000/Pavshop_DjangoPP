from django.db.models import CheckConstraint, CharField, ForeignKey, SlugField, BooleanField, IntegerField, DecimalField, ManyToManyField, DateField, TextField, ImageField, PROTECT, CASCADE, Q, F
from django.utils import timezone
from django.urls import reverse_lazy


from core.Abstact_models import AbstractModel
from account.models import User


class Category(AbstractModel):
    title = CharField(max_length=50, db_index=True, verbose_name='Category')
    parent = ForeignKey('self', on_delete=CASCADE, null=True, blank=True, parent_link='parents', related_name='parents')
    slug = SlugField(max_length=100, unique=True, db_index=True, verbose_name='Category_slug')
    user = ForeignKey(User, on_delete=PROTECT)
    
    def get_absolute_url(self):
        return reverse_lazy('product_list', kwargs={'category':self.title})
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        unique_together = ['title', 'parent']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['title']


class DiscountType(AbstractModel):
    title = CharField(max_length=50, unique=True, verbose_name='Discont')
    user = ForeignKey(User, on_delete=PROTECT)
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self, **kwargs):
        return reverse_lazy('product', kwargs={'discounttype': self.title })

    
class Discount(AbstractModel):
    title = CharField(max_length=100, unique=True, verbose_name='Discont')
    code = CharField(max_length=50, blank=True, unique=True) #
    type_id = ForeignKey(DiscountType, on_delete=PROTECT, related_name='types') #
    amount = IntegerField(blank=True) # кол-во продуктов которая должна быть в ордере что бы получитть скидку
    decrease_by = DecimalField(max_digits=10, decimal_places=2, blank=True) # сумма на которую надо снизить стоимость
    price_sum = DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # сумму которую надо набрать что бы активировать скидку
    other_product = ForeignKey('Product', blank=True, null=True, on_delete=CASCADE) # подарок
    discount_persent = DecimalField(max_digits=8, blank=True, decimal_places=2) # процент скидки на которую надо снизить стоимость товара  
    date_begin = DateField() 
    date_end = DateField() 
    user = ForeignKey(User, on_delete=PROTECT)
    deleted_at = BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('product/', kwargs={'product':self.title})

    class Meta:
        verbose_name = 'discont'
        verbose_name_plural = 'disconts'
        ordering = ['-pk']
        constraints = [
            CheckConstraint(
                check = Q(discount_persent__lte=100), 
                name = 'persent',
            ),
        ]

class ProductReview(AbstractModel):
    user = ForeignKey(User, on_delete=PROTECT, verbose_name='User', related_name='userreview')
    product = ForeignKey('Product', on_delete=PROTECT, related_name='productreview')
    review = ForeignKey('self', on_delete=CASCADE, null=True, blank=True, parent_link='review')
    text = TextField()
    rating = DecimalField(max_digits=4, decimal_places=3, blank=True)
    published_at = BooleanField(default=False)
    deleted_at = BooleanField(default=False)
  
    def __str__(self) -> str:
        return f'{self.user} {self.product} {self.review}'
    
    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
        ordering = ['pk']
        constraints = [
            CheckConstraint(
                check = Q(rating__lt=5), 
                name = 'rating_data',
            ),
        ]


class Store(AbstractModel):
    title = CharField(max_length=50, unique=True, default='Pavshop')
    address = CharField(max_length=100, unique=True)
    post = CharField(max_length=6, blank=True)
    location = CharField(max_length=255, blank=True, unique=True)
    user = ForeignKey(User, on_delete=PROTECT)
    deleted_at = BooleanField(default=False)
   
    def __str__(self) -> str:
        return f'{self.title} {self.address}'
    
    class Meta:
        verbose_name = 'store'
        verbose_name_plural = 'stores'
        ordering = ['title']

class Unit(AbstractModel):
    title = CharField(max_length=100, unique=True)
    user = ForeignKey(User, on_delete=PROTECT)

    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
    
    def __str__(self) -> str:
        return self.title


class Color(AbstractModel):
    title = CharField(max_length=50, unique=True, db_index=True, verbose_name='Color')
    slug = SlugField(max_length=100, unique=True, db_index=True, verbose_name='color_slug')
    user = ForeignKey(User, on_delete=PROTECT)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'
        ordering = ['title']


class Designer(AbstractModel):
    name = CharField(max_length=100, unique=True, db_index=True, verbose_name='Designer')
    slug = SlugField(max_length=100, unique=True, db_index=True, verbose_name='Varian_slug')
    user = ForeignKey(User, on_delete=PROTECT)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('designer', kwargs={'designer':self.title})

    class Meta:
        verbose_name = 'designer'
        verbose_name_plural = 'designers'
        ordering = ['name']


class Style(AbstractModel):
    title = CharField(max_length=50, unique=True, db_index=True, verbose_name='Style')
    slug = SlugField(max_length=100, unique=True, db_index=True)
    user = ForeignKey(User, on_delete=PROTECT)
   
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('style', kwargs={'style':self.title})

    class Meta:
        verbose_name = 'style'
        verbose_name_plural = 'styles'
        ordering = ['title']


class Brand(AbstractModel):
    title = CharField(max_length=50, unique=True, db_index=True, verbose_name='Brand')  
    slug = SlugField(max_length=100, unique=True, db_index=True)
    user = ForeignKey(User, on_delete=PROTECT)
    deleted_at = BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('brand', kwargs={'brand':self.title})
    
    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
        ordering = ['title']


class Collection(AbstractModel):
    title = CharField(max_length=100, db_index=True)
    brand_id = ForeignKey(Brand, on_delete=PROTECT)
    slug = SlugField(max_length=100, unique=True, db_index=True)
    user = ForeignKey(User, on_delete=PROTECT)
    deleted_at = BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.brand_id} {self.title}'
    
    def get_absolute_url(self):
        return reverse_lazy('collection', kwargs={'collection':self.title})

    class Meta:
        unique_together = ['title', 'brand_id']
        verbose_name = 'collection'
        verbose_name_plural = 'collections'
        ordering = ['brand_id']


class Tag(AbstractModel):
    title = CharField(max_length=20, unique=True, db_index=True, verbose_name='Tag')
    user = ForeignKey(User, on_delete=PROTECT)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('tag', kwargs={'tag': self.title})


class Product(AbstractModel): #11
    title = CharField(max_length=50, unique=True, db_index=True, verbose_name='Product')
    slug = SlugField(max_length=100, unique=True, db_index=True)
    category_id = ManyToManyField('Category', related_name='category')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='fabric price')
    brand_id = ForeignKey(Brand, on_delete=PROTECT, blank=True, null=True, related_name='brand')
    designer = ForeignKey(Designer, on_delete=PROTECT, blank=True, null=True)
    collection_id = ForeignKey(Collection, on_delete=CASCADE, blank=True, null=True, related_name='collection')
    description = TextField(blank=True, verbose_name='Description')
    archive = BooleanField(default=False, verbose_name='Archived')
    style_id = ForeignKey(Style, on_delete=PROTECT, blank=True, null=True, related_name='style')
    tag = ManyToManyField(Tag, related_name='product_tag', blank=True)
    parent = ManyToManyField('self', blank=True)
    user = ForeignKey(User, on_delete=PROTECT, related_name='user_add_product', verbose_name='product_creator')
    publised_at = BooleanField(default=True)
    deleted_at = BooleanField(default=False)

    def get_absolute_url(self):
        return reverse_lazy('product/', kwargs={'product':self.title})
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['-pk']


class Image(AbstractModel):
    image = ImageField(upload_to='blog_image/', verbose_name='Image')
    user = ForeignKey(User, on_delete=PROTECT, verbose_name='creater', related_name='user_add_image')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ['pk']

    def __str__(self) -> str:
        return f'{self.image}'

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={'image':f'{self.image}'})


class Variant(AbstractModel):
    title = CharField(max_length=100, unique=True, db_index=True, verbose_name='variant')
    color = ForeignKey(Color, on_delete=CASCADE, verbose_name='color')
    slug = SlugField(max_length=100, unique=True, db_index=True, verbose_name='Varian_slug')
    image_id = ManyToManyField(Image, verbose_name='Image')
    product_id = ForeignKey(Product, on_delete=CASCADE)
    price = DecimalField(max_digits=10, decimal_places=2, db_index=True, verbose_name='price')
    discount_id = ManyToManyField(Discount, verbose_name='Discont', blank=True)
    unit = ForeignKey(Unit, on_delete=PROTECT, null=True, verbose_name='Unit')
    tag = ManyToManyField(Tag, related_name='variant_tag')
    parent = ManyToManyField('self', blank=True)
    user = ForeignKey(User, on_delete=PROTECT, related_name='user_add_variant', verbose_name='variant_creator')
  
    def get_absolute_url(self):
        return reverse_lazy('variant', kwargs={'product':self.title})
    
    def __str__(self) -> str:
        return f'{self.title} color:{self.color} ({self.unit})'
    
    class Meta:
        verbose_name = 'variant'
        verbose_name_plural = 'variants'
        ordering = ['title']


class VariantToStore(AbstractModel):
    variant = ForeignKey(Variant, on_delete=CASCADE, verbose_name='variant', related_name='varianttostore')
    store = ForeignKey(Store, on_delete=CASCADE, verbose_name='store', related_name='variantinstore')
    quantity = IntegerField()

    class Meta:
        unique_together = ['variant', 'store']
        verbose_name = 'variant to store'
        verbose_name_plural = 'variant to stores'
        ordering = ['store']

    def __str__(self) -> str:
        return f'{self.variant} sotore:{self.store}, quantity:{self.quaantity}'

