# Generated by Django 4.2.3 on 2023-11-01 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_producttobasket_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='address_delivery', to='account.address', verbose_name='delivery_address'),
        ),
    ]
