from django.urls import path
from doctors import views

urlpatterns = [
    path('',views.alldoctors,name='alldoctors'),
    path('treatments', views.all_treatments, name='all_treatments'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('treatment/<int:id>/', views.doctors_by_treatment, name='doctors_by_treatment'),
    path('book-doctor/<int:doctor_id>/<int:treatment_id>/', views.book_doctor, name='book_doctor')
]