from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class AttendanceRecordType(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    description = models.TextField(_('description'), blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('record type')
        verbose_name_plural = _('record types')

    def __str__(self):
        return self.name

class AttendanceAccessType(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    description = models.TextField(_('description'), blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('access type')
        verbose_name_plural = _('access types')

    def __str__(self):
        return self.name

class Attendance(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('user'),
        related_name='attendance_records'
    )
    store = models.ForeignKey(
        'stores.Store',
        on_delete=models.CASCADE,
        verbose_name=_('store')
    )
    record_type = models.ForeignKey(
        AttendanceRecordType,
        on_delete=models.CASCADE,
        verbose_name=_('record type')
    )
    access_type = models.ForeignKey(
        AttendanceAccessType,
        on_delete=models.CASCADE,
        verbose_name=_('access type')
    )
    photo = models.ImageField(
        _('photo'),
        upload_to='attendance_photos/',
        blank=True,
        null=True,
        help_text=_('Photo captured during attendance record')
    )
    automatic = models.BooleanField(
        _('automatic'),
        default=False,
        help_text=_('Indicates if the record was automatic')
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('attendance record')
        verbose_name_plural = _('attendance records')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} - {self.record_type.name} ({self.access_type.name})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)