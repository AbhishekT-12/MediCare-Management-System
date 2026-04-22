from django import forms
from payment.models import Admission

class Discharge_summary_form(forms.ModelForm):
    class Meta:
        model = Admission
        fields = [
            'patient_name',
            'doctor_name',
            'treatment',
            'description',
            'date_of_admitted',
            'date_of_discharge',
            'room_type',
            'food_required',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_of_admitted': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_of_discharge': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_discharge'].required = True

        for field_name, field in self.fields.items():
            if field_name not in self.Meta.widgets and field_name != 'food_required':
                field.widget.attrs.update({'class': 'form-control'})

        self.fields['food_required'].widget.attrs.update({'class': 'form-check-input'})

    def clean(self):
        cleaned_data = super().clean()
        date_of_admitted = cleaned_data.get('date_of_admitted')
        date_of_discharge = cleaned_data.get('date_of_discharge')

        if date_of_admitted and date_of_discharge and date_of_discharge < date_of_admitted:
            self.add_error('date_of_discharge', 'Discharge date cannot be before admission date.')

        return cleaned_data
