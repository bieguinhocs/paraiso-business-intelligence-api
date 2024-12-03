# Generated by Django 4.2.14 on 2024-11-27 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0014_alter_store_promoters'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceAccessType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'access type',
                'verbose_name_plural': 'access types',
            },
        ),
        migrations.CreateModel(
            name='AttendanceRecordType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'record type',
                'verbose_name_plural': 'record types',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, help_text='Photo captured during attendance record', null=True, upload_to='attendance_photos/', verbose_name='photo')),
                ('automatic', models.BooleanField(default=False, help_text='Indicates if the record was automatic', verbose_name='automatic')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('access_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendances.attendanceaccesstype', verbose_name='access type')),
                ('record_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendances.attendancerecordtype', verbose_name='record type')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.store', verbose_name='store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_records', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'attendance record',
                'verbose_name_plural': 'attendance records',
                'ordering': ['-created_at'],
            },
        ),
    ]
