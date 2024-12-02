from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'photo' in self.fields:
            self.fields['photo'].widget.attrs.update({
                'accept': 'image/*',
                'capture': 'camera',
            })