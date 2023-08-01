# Generated by Django 4.2.3 on 2023-08-01 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Brand')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Category')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link='parents', related_name='parents', to='product.category')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Category_slug')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.brand')),
            ],
            options={
                'verbose_name': 'collection',
                'verbose_name_plural': 'collections',
                'ordering': ['brand_id'],
                'unique_together': {('title', 'brand_id')},
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Color')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='color_slug')),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Designer')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Varian_slug')),
            ],
            options={
                'verbose_name': 'designer',
                'verbose_name_plural': 'designers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Discont')),
                ('code', models.CharField(max_length=50)),
                ('sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_begin', models.DateField()),
                ('date_end', models.DateField()),
            ],
            options={
                'verbose_name': 'discont',
                'verbose_name_plural': 'disconts',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='DiscountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Discont')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('image_url', models.ImageField(db_index=True, unique=True, upload_to='product_images/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Product')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='fabric price')),
                ('views', models.IntegerField(null=True, verbose_name='viewer')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('archive', models.BooleanField(default=False, verbose_name='Archived')),
                ('brand_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='brand', to='product.brand')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category', to='product.category')),
                ('collection_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='product.collection')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('title', models.CharField(default='Pavshop', max_length=50, unique=True)),
                ('address', models.CharField(max_length=100, unique=True)),
                ('post', models.IntegerField(blank=True)),
                ('location', models.CharField(blank=True, max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'store',
                'verbose_name_plural': 'stores',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Style')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'style',
                'verbose_name_plural': 'styles',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='variant')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Varian_slug')),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=10, verbose_name='price')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.color', verbose_name='color')),
                ('discont_id', models.ManyToManyField(to='product.discount', verbose_name='Discont')),
                ('image_id', models.ManyToManyField(to='product.image', verbose_name='Image')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('tag', models.ManyToManyField(related_name='variant_tag', to='core.tag')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.unit', verbose_name='Unit')),
            ],
            options={
                'verbose_name': 'variant',
                'verbose_name_plural': 'variants',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('text', models.TextField()),
                ('rating', models.DecimalField(blank=True, decimal_places=3, max_digits=5)),
                ('published_at', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productreview', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userreview', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
                'ordering': ['pk'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='style_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='style', to='product.style'),
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(related_name='product_tag', to='core.tag'),
        ),
        migrations.AddField(
            model_name='discount',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='types', to='product.discounttype'),
        ),
    ]
