# Generated by Django 4.2.14 on 2024-10-28 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_alter_sale_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sale_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.salestatus', verbose_name='status'),
        ),
    ]