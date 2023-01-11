from django import forms
from .models import Appointments


class DateForm(forms.DateInput):
    input_type = 'date'
    # is_visible = False
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['username', 'email', 'service', 'date', 'appointment_time']
        widgets = {
            'date': DateForm()
        }