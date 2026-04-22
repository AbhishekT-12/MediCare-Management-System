from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.labtech_dashboard, name='labtech_dashboard'),
    path('all-tests/', views.all_tests, name='all_tests'),
    path('add-hospital-test/', views.add_hospital_test, name='add_hospital_test'),
    path('pending/', views.pending_tests, name='pending_tests'),
    path('add-test/', views.add_lab_test, name='add_lab_test'),
    path('edit-test/<int:test_id>/', views.edit_lab_test, name='edit_lab_test'),
]
