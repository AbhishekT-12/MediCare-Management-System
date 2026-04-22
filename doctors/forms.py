from django import forms
from doctors.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time_slot', 'consultation_charge']

        widgets = {
            'date':forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'consultation_charge': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['consultation_charge'].disabled = True
