from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from decimal import Decimal
from .forms import Discharge_summary_form
from .models import Admission

# Create your views here.

ROOM_CHARGES = {
    'Common Ward': {
        'bed_charge': 250,
        'nursing_charge': 300,
        'doctor_visit': 250,
        'misc_charge': 100,
        'medicine_percent': 10,
    },
    'Semi-Private': {
        'bed_charge': 1000,
        'nursing_charge': 1000,
        'doctor_visit': 550,
        'misc_charge': 250,
        'medicine_percent': 12,
    },
    'Private AC': {
        'bed_charge': 1500,
        'nursing_charge': 1250,
        'doctor_visit': 650,
        'misc_charge': 350,
        'medicine_percent': 16,
    },
    'Private Non AC': {
        'bed_charge': 1250,
        'nursing_charge': 1150,
        'doctor_visit': 650,
        'misc_charge': 300,
        'medicine_percent': 14,
    },
    'Deluxe': {
        'bed_charge': 2000,
        'nursing_charge': 1500,
        'doctor_visit': 850,
        'misc_charge': 500,
        'medicine_percent': 20,
    },
}

FOOD_CHARGE_PER_DAY = 480


def calculate_bill(admission):
    charges = ROOM_CHARGES[admission.room_type]
    total_days = max((admission.date_of_discharge - admission.date_of_admitted).days, 1)

    bed_total = charges['bed_charge'] * total_days
    nursing_total = charges['nursing_charge'] * total_days
    doctor_total = charges['doctor_visit'] * total_days
    misc_total = charges['misc_charge'] * total_days
    food_total = FOOD_CHARGE_PER_DAY * total_days if admission.food_required else 0
    room_total = bed_total + nursing_total + doctor_total + misc_total
    subtotal = room_total + food_total
    medicine_charge = (Decimal(subtotal) * Decimal(charges['medicine_percent']) / Decimal(100)).quantize(Decimal('0.01'))
    grand_total = Decimal(subtotal) + medicine_charge

    return {
        'charges': charges,
        'total_days': total_days,
        'food_charge_per_day': FOOD_CHARGE_PER_DAY,
        'bed_total': bed_total,
        'nursing_total': nursing_total,
        'doctor_total': doctor_total,
        'misc_total': misc_total,
        'food_total': food_total,
        'room_total': room_total,
        'subtotal': subtotal,
        'medicine_charge': medicine_charge,
        'grand_total': grand_total,
    }

@login_required(login_url='login')
def discharge(request):
    if request.method == 'POST':
        form = Discharge_summary_form(request.POST)
        if form.is_valid():
            admission = form.save(commit=False)
            admission.total_days = max((admission.date_of_discharge - admission.date_of_admitted).days, 1)
            admission.save()
            return redirect('final_bill', admission_id=admission.id)
    else:
        form = Discharge_summary_form()

    return render(request, 'discharge.html', {'form': form})


@login_required(login_url='login')
def final_bill(request, admission_id):
    admission = get_object_or_404(Admission, id=admission_id)
    bill = calculate_bill(admission)

    return render(request, 'final_bill.html', {
        'admission': admission,
        'bill': bill,
        'hospital_name': 'Medicare HMS Hospital',
        'hospital_address': 'Main Road, City Center, India',
    })
