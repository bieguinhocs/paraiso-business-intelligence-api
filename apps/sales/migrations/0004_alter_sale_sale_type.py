# Generated by Django 4.2.14 on 2024-10-28 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_sale_sale_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sale_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.saletype', verbose_name='type'),
        ),
    ]