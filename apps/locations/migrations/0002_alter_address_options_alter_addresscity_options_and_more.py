# Generated by Django 4.2.14 on 2024-08-24 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Dirección', 'verbose_name_plural': '5. Direcciones'},
        ),
        migrations.AlterModelOptions(
            name='addresscity',
            options={'verbose_name': 'Ciudad', 'verbose_name_plural': '2. Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='addressdepartment',
            options={'verbose_name': 'Departamento', 'verbose_name_plural': '1. Departamentos'},
        ),
        migrations.AlterModelOptions(
            name='addressdistrict',
            options={'verbose_name': 'Distrito', 'verbose_name_plural': '4. Distritos'},
        ),
        migrations.AlterModelOptions(
            name='addresszonegroup',
            options={'verbose_name': 'Grupo Zonal', 'verbose_name_plural': '3. Grupos Zonales'},
        ),
    ]
