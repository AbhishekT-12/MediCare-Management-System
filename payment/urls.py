from django.urls import path
from payment import views

urlpatterns = [
    path('discharge/', views.discharge, name='discharge'),
    path('final-bill/<int:admission_id>/', views.final_bill, name='final_bill'),
]
