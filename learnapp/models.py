from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # FIX 2: blank=True, null=True so update form can save without all fields filled
    phone   = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True)
    street  = models.CharField(max_length=100, blank=True)
    city    = models.CharField(max_length=100, blank=True)
    state   = models.CharField(max_length=100, blank=True)
    zipcode = models.IntegerField(blank=True, null=True)
    userpic = models.ImageField(upload_to='userimg', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} – Details"