# Generated by Django 4.2.3 on 2023-08-24 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_variant_discount_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='designer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.designer'),
        ),
    ]
