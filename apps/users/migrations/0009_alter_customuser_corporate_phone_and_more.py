# Generated by Django 4.2.14 on 2024-12-03 19:15

import django.core.validators
from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_supervisor_customuser_coordinator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='corporate_phone',
            field=models.CharField(blank=True, max_length=9, null=True, validators=[utils.validators.validate_only_digits, django.core.validators.MinLengthValidator(9)], verbose_name='corporate phone number'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='document_type',
            field=models.CharField(choices=[('DNI', 'Documento Nacional de Identidad'), ('CE', 'Carnet de Extranjería')], max_length=3, verbose_name='document type'),
        ),
    ]
