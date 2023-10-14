# Generated by Django 4.2.3 on 2023-10-07 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_alter_image_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.variant', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='varianttostore',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store', to='product.store', verbose_name='store'),
        ),
    ]
