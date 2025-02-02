# Generated by Django 4.2.3 on 2023-08-23 15:09

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='phone')),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/')),
                ('saller', models.BooleanField(default=False, verbose_name='Saller')),
                ('bloger', models.BooleanField(default=False, verbose_name='Bloger')),
                ('deleted_at', models.BooleanField(default=False, verbose_name='delete Account')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ['-pk'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('company_name', models.CharField(blank=True, max_length=50, verbose_name='Company')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('city', models.CharField(max_length=50, verbose_name='City/Town')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('deleted_at', models.BooleanField(default=False, verbose_name='delete at Address')),
            ],
            options={
                'verbose_name': 'user_address',
                'verbose_name_plural': 'addresses',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='ProductToBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('count', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Count')),
            ],
            options={
                'verbose_name': 'product_to_basket',
                'verbose_name_plural': 'products_to_basket',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Order status')),
            ],
            options={
                'verbose_name': 'status',
                'verbose_name_plural': 'statuses',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('deleted_at', models.BooleanField(db_index=True, default=False, verbose_name='delete at from Wishlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlistuser', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'users_wishs',
                'verbose_name_plural': 'wishlists',
                'ordering': ['-pk'],
            },
        ),
    ]
