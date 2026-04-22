from django.contrib import admin
from .models import Lab_Test, Lab_Tech, HospitalTest

admin.site.register(Lab_Tech)
admin.site.register(Lab_Test)
admin.site.register(HospitalTest)
