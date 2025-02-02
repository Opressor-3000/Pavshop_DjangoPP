# Generated by Django 4.2.3 on 2023-10-20 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_alter_image_variant_alter_varianttostore_store'),
        ('blog', '0002_alter_post_category_alter_post_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='categories', to='product.category', verbose_name='About Categories'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='product.tag', verbose_name='Tags'),
        ),
    ]
