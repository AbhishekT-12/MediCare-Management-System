from django.db import models

# Create your models here.

class Admission(models.Model):
    ROOM_CHOICES = [
        ('Common Ward', 'Common Ward'),
        ('Semi-Private', 'Semi-Private'),
        ('Private Non AC', 'Private Non AC'),
        ('Private AC', 'Private AC'),
        ('Deluxe', 'Deluxe'),
    ]

    patient_name = models.ForeignKey(
        'learnapp.UserDetails',
        on_delete=models.CASCADE,
        related_name='admissions'
    )
    doctor_name = models.ForeignKey(
        'doctors.ALLDOCTORS',
        on_delete=models.CASCADE,
        related_name='admissions'
    )
    treatment = models.ForeignKey(
        'doctors.Treatment',
        on_delete=models.CASCADE,
        related_name='admissions'
    )
    description = models.TextField(blank=True)
    date_of_admitted = models.DateField()
    date_of_discharge = models.DateField(blank=True, null=True)
    room_type = models.CharField(max_length=50, choices=ROOM_CHOICES, default='Common Ward')
    food_required = models.BooleanField(default=False)
    total_days = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient_name} - {self.doctor_name} ({self.date_of_admitted})"
