from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import ALLDOCTORS,Treatment
from .forms import AppointmentForm

# Create your views here.

def alldoctors(request):
    doctors = ALLDOCTORS.objects.all()
    return render(request,"doctors/alldoctors.html",{'doctors':doctors})


def all_treatments(request):
    treatments = Treatment.objects.all()
    return render(request, 'doctors/treatments.html', {'treatments': treatments})

# Page 1: Show all treatments
def book_appointment(request):
    treatments = Treatment.objects.all()
    return render(request, 'doctors/book_appointment.html', {'treatments': treatments})


# Page 2: Show doctors based on treatment
def doctors_by_treatment(request, id):
    treatment = get_object_or_404(Treatment, id=id)
    doctors = ALLDOCTORS.objects.filter(specialisation = treatment.category)
    # doctors = [treatment.doctor]

    return render(request, 'doctors/doctors_by_treatment.html', {
        'treatment': treatment,
        'doctors': doctors
    })



@login_required(login_url='login')
def book_doctor(request, doctor_id,treatment_id):
    doctor = get_object_or_404(ALLDOCTORS, id=doctor_id)
    treatment = get_object_or_404(Treatment, id=treatment_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.doctor = doctor
            appointment.treatment = treatment
            appointment.save()
            return redirect('alldoctors')  # or success page
    else:
        form = AppointmentForm()

    return render(request, 'doctors/book_form.html', {
        'form': form,
        'doctor': doctor,
        'treatment': treatment,
    })
