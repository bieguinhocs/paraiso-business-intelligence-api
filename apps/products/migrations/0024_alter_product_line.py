# Generated by Django 4.2.14 on 2024-09-10 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_remove_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productline', verbose_name='line'),
        ),
    ]
