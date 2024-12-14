# Generated by Django 4.2.14 on 2024-09-09 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_product_nombre_único_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='productline',
            name='unique_name_not_dash',
        ),
        migrations.AddConstraint(
            model_name='productline',
            constraint=models.UniqueConstraint(condition=models.Q(('name', '-'), _negated=True), fields=('name',), name='nombre único'),
        ),
    ]