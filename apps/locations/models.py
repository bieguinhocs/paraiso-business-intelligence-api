from django.db import models

class AddressDepartment(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nombre')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creación de registro')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.name

class AddressCity(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nombre')
    department = models.ForeignKey(AddressDepartment, on_delete=models.CASCADE, verbose_name='Departamento')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creación de registro')

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.name

class AddressZoneGroup(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nombre')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creación de registro')

    class Meta:
        verbose_name = 'Grupo Zonal'
        verbose_name_plural = 'Grupos Zonales'

    def __str__(self):
        return self.name

class AddressDistrict(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    city = models.ForeignKey(AddressCity, on_delete=models.CASCADE, verbose_name='Ciudad')
    zone_group = models.ForeignKey(AddressZoneGroup, on_delete=models.CASCADE, verbose_name='Grupo zonal')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creación de registro')

    class Meta:
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'

    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nombre')
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ubicación')
    district = models.ForeignKey(AddressDistrict, on_delete=models.CASCADE, verbose_name='Distrito')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creación de registro')

    class Meta:
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'

    def __str__(self):
        return self.name or self.location
 