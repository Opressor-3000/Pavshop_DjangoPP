# Generated by Django 4.2.3 on 2023-07-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
                ('phone', models.CharField(max_length=12, unique=True, verbose_name='Contact Phone')),
                ('subject', models.CharField(max_length=50, verbose_name='subject')),
                ('message', models.TextField(verbose_name='message')),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('email', models.EmailField(db_index=True, max_length=50, unique=True, verbose_name='subscriber')),
            ],
            options={
                'verbose_name': 'subscriber',
                'verbose_name_plural': 'subscribers',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('title', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
