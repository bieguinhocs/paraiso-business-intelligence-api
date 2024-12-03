# Generated by Django 4.2.14 on 2024-09-12 08:09

from django.db import migrations, models
import stores.validators


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0011_alter_storeretail_ruc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='code',
            field=models.CharField(blank=True, max_length=6, unique=True, validators=[stores.validators.validate_alpha_numeric_code], verbose_name='code'),
        ),
    ]
