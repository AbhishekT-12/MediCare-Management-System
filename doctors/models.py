from django.conf import settings
from django.db import models

# Create your models here.
class ALLDOCTORS(models.Model):

    SPECIALIZATIONS = [
        ('General Medicine', 'General Medicine'),
        ('Ortho', 'Ortho'),
        ('ENT', 'ENT'),
        ('Eye Specialist', 'Eye Specialist'),
        ('Dentist', 'Dentist'),
        ('Others', 'Others'),
    ]

    name = models.CharField(max_length=100)
    specialisation = models.CharField(choices=SPECIALIZATIONS)
    experience = models.PositiveIntegerField()  # years of experience
    licence_no = models.CharField(max_length=100, unique=True)
    certificate = models.FileField(upload_to='certificates',blank=True,null=True)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()

    def __str__(self):
        return self.name

class Treatment(models.Model):

    CATEGORY_CHOICES = [
        ('General Medicine', 'General Medicine'),
        ('Ortho', 'Ortho'),
        ('ENT', 'ENT'),
        ('Eye Specialist', 'Eye Specialist'),
        ('Dentist', 'Dentist'),
        ('Others', 'Others'),
    ]

    treatment_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    doctor = models.ForeignKey(ALLDOCTORS, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.treatment_name


class Appointment(models.Model):

    TIME_SLOTS = [
        ('9AM-11AM', '9AM-11AM'),
        ('11AM-1PM', '11AM-1PM'),
        ('2PM-4PM', '2PM-4PM'),
        ('4PM-6PM', '4PM-6PM'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='appointments')
    doctor = models.ForeignKey(ALLDOCTORS, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    time_slot = models.CharField(max_length=20, choices=TIME_SLOTS)
    consultation_charge = models.PositiveIntegerField(default=550)

    def __str__(self):
        return f"{self.doctor.name} - {self.date}"