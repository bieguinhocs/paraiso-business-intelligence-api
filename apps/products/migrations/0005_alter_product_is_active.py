# Generated by Django 4.2.14 on 2024-09-09 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(help_text='Indicates whether this product is active. Uncheck this option if it is not active.', verbose_name='status'),
        ),
    ]
