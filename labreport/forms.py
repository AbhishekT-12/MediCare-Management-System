from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from labreport.models import Lab_Tech

class LabTechRegistrationForm(UserCreationForm):
    empid = forms.IntegerField()
    qualification = forms.CharField(max_length=100)
    address = forms.CharField(max_length=200)
    yoe = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self):
        user = super().save(commit=False)
        user.save()

        empid = self.cleaned_data['empid']
        qualification = self.cleaned_data['qualification']
        yoe = self.cleaned_data['yoe']
        address = self.cleaned_data['address']

        Lab_Tech.objects.create(
            user=user,
            empId=empid,
            qualification=qualification,
            years_of_exp=yoe,
            address=address
        )
        return user