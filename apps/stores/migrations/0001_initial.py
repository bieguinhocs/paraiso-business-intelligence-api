# Generated by Django 4.2.14 on 2024-09-05 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0004_rename_addresszonegroup_addresszonalgroup_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'store channel',
                'verbose_name_plural': 'store channels',
            },
        ),
        migrations.CreateModel(
            name='StoreCoverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'store coverage',
                'verbose_name_plural': 'store coverages',
            },
        ),
        migrations.CreateModel(
            name='StoreRetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('business_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='business name')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.storechannel', verbose_name='channel')),
            ],
            options={
                'verbose_name': 'store retail',
                'verbose_name_plural': 'store retails',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('sellout_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='sellout name')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.address', verbose_name='address')),
                ('coordinator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coordinator_stores', to=settings.AUTH_USER_MODEL, verbose_name='coordinator')),
                ('coverage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.storecoverage', verbose_name='coverage')),
                ('promoters', models.ManyToManyField(related_name='promoter_stores', to=settings.AUTH_USER_MODEL, verbose_name='promoters')),
                ('retail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.storeretail', verbose_name='retail')),
            ],
            options={
                'verbose_name': 'store',
                'verbose_name_plural': 'stores',
            },
        ),
    ]