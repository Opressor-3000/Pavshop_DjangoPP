# Generated by Django 4.2.3 on 2023-08-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_views_alter_discount_discount_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='discount_id',
            field=models.ManyToManyField(blank=True, to='product.discount', verbose_name='Discont'),
        ),
    ]
