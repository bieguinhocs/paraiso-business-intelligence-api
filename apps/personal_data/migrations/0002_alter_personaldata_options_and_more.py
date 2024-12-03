# Generated by Django 4.2.14 on 2024-12-03 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personaldata',
            options={'ordering': ['-created_at'], 'verbose_name': 'personal data survey', 'verbose_name_plural': 'personal data surveys'},
        ),
        migrations.RenameField(
            model_name='personaldata',
            old_name='client_document',
            new_name='client_document_number',
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='client_document_type',
            field=models.CharField(choices=[('DNI', 'Documento Nacional de Identidad'), ('CE', 'Carnet de Extranjería')], max_length=3, verbose_name='document type'),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='photo',
            field=models.ImageField(help_text='Photo of the personal data survey', upload_to='personal_data_survey_photos/', verbose_name='photo'),
        ),
    ]
