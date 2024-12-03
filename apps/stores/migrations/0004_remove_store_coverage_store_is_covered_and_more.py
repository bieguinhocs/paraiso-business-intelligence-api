# Generated by Django 4.2.14 on 2024-09-05 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_alter_storechannel_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='coverage',
        ),
        migrations.AddField(
            model_name='store',
            name='is_covered',
            field=models.BooleanField(default=False, verbose_name='coverage'),
        ),
        migrations.DeleteModel(
            name='StoreCoverage',
        ),
    ]
