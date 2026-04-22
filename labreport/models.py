from django.db import models
from doctors.models import ALLDOCTORS
from learnapp.models import UserDetails
from django.conf import settings

LAB_TEST_CHOICES = [
    ('CBC', 'CBC'),
    ('LFT', 'LFT'),
    ('urine total test', 'Urine Total Test'),
    ('urine microscopic', 'Urine Microscopic'),
    ('serum routine', 'Serum Routine'),
    ('thyroid', 'Thyroid'),
]

TEST_RANGE_CHOICES = [
    ('Nil', 'Nil'),
    ('positive', 'Positive'),
    ('negative', 'Negative'),
    ('abnormal', 'Abnormal'),
]


class Lab_Tech(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    empId = models.IntegerField()
    qualification = models.CharField(max_length=200)
    years_of_exp = models.IntegerField()
    address = models.CharField(max_length=300)


# ── Hospital test catalog (shown in All Tests page) ──────────────────────────
class HospitalTest(models.Model):
    test_name = models.CharField(max_length=200)
    price = models.IntegerField()
    time_required = models.CharField(max_length=100, default='1-2 hours')

    def __str__(self):
        return self.test_name


# ── Doctor-referred patient tests (shown in Dashboard) ───────────────────────
class Lab_Test(models.Model):
    referred_by = models.ForeignKey(ALLDOCTORS, on_delete=models.CASCADE)
    patient_name = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    lab_test = models.CharField(max_length=200, choices=LAB_TEST_CHOICES, default='CBC')
    lab_result = models.CharField(max_length=200, choices=[
        ('pending', 'Pending'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    test_range = models.CharField(max_length=200, choices=TEST_RANGE_CHOICES, default='Nil')
    result_desc = models.TextField(blank=True)
    test_cost = models.IntegerField()
    time_required = models.CharField(max_length=100, default='1-2 hours')
