from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    dni = models.CharField(max_length=255, unique=True)
    corporate_email = models.EmailField(blank=True, null=True)
    corporate_phone = models.CharField(max_length=255, blank=True, null=True)
    corporate_device_imei = models.CharField(max_length=255, blank=True, null=True)
    employment_start_date = models.DateTimeField(blank=True, null=True)
    employment_end_date = models.DateTimeField(blank=True, null=True)
    address = models.ForeignKey('locations.Address', on_delete=models.SET_NULL, null=True, blank=True)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
