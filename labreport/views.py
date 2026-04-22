from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lab_Test, HospitalTest
from doctors.models import ALLDOCTORS
from learnapp.models import UserDetails
from django.core.paginator import Paginator


# ================= DASHBOARD (doctor-referred tests) =================
@login_required
def labtech_dashboard(request):
    all_lab_tests = Lab_Test.objects.all().order_by('-created_at')

    paginator = Paginator(all_lab_tests, 4)
    page_number = request.GET.get('pg')
    tests = paginator.get_page(page_number)

    context = {
        'tests': tests,
        'pending_count': all_lab_tests.filter(lab_result='pending').count(),
        'ongoing_count': all_lab_tests.filter(lab_result='ongoing').count(),
        'completed_count': all_lab_tests.filter(lab_result='completed').count(),
    }
    return render(request, 'labreport/dashboard.html', context)


# ================= ALL TESTS (hospital catalog) =================
@login_required
def all_tests(request):
    tests = HospitalTest.objects.all()
    return render(request, 'labreport/all_tests.html', {'tests': tests})


@login_required
def add_hospital_test(request):
    if request.method == 'POST':
        test_name = request.POST.get('test_name')
        price = request.POST.get('price')
        time_required = request.POST.get('time_required')

        if test_name and price:
            HospitalTest.objects.create(
                test_name=test_name,
                price=price,
                time_required=time_required or '1-2 hours'
            )
            return redirect('all_tests')

    return render(request, 'labreport/add_hospital_test.html')


# ================= PENDING TESTS =================
@login_required
def pending_tests(request):
    tests = Lab_Test.objects.filter(lab_result='pending').order_by('-created_at')
    return render(request, 'labreport/dashboard.html', {
        'tests': tests,
        'pending_count': tests.count(),
        'ongoing_count': 0,
        'completed_count': 0,
    })


# ================= ADD LAB TEST (refer test to patient) =================
@login_required
def add_lab_test(request):
    if request.method == 'POST':
        Lab_Test.objects.create(
            referred_by_id=request.POST.get('doctor'),
            patient_name_id=request.POST.get('patient'),
            lab_test=request.POST.get('lab_test'),
            test_cost=request.POST.get('cost'),
            time_required=request.POST.get('time_required', '1-2 hours'),
            result_desc=request.POST.get('desc', ''),
            lab_result='pending'
        )
        return redirect('labtech_dashboard')

    doctors = ALLDOCTORS.objects.all()
    patients = UserDetails.objects.all()
    hospital_tests = HospitalTest.objects.all()

    return render(request, 'labreport/add_lab_test.html', {
        'doctors': doctors,
        'patients': patients,
        'hospital_tests': hospital_tests,
    })


# ================= EDIT LAB TEST (edit existing, not create new) =================
@login_required
def edit_lab_test(request, test_id):
    test = get_object_or_404(Lab_Test, id=test_id)

    if request.method == 'POST':
        test.referred_by_id = request.POST.get('doctor')
        test.patient_name_id = request.POST.get('patient')
        test.lab_test = request.POST.get('lab_test')
        test.test_cost = request.POST.get('cost')
        test.time_required = request.POST.get('time_required', '1-2 hours')
        test.result_desc = request.POST.get('desc', '')
        test.lab_result = request.POST.get('lab_result', test.lab_result)
        test.save()
        return redirect('labtech_dashboard')

    doctors = ALLDOCTORS.objects.all()
    patients = UserDetails.objects.all()
    hospital_tests = HospitalTest.objects.all()

    return render(request, 'labreport/edit_lab_test.html', {
        'test': test,
        'doctors': doctors,
        'patients': patients,
        'hospital_tests': hospital_tests,
    })
