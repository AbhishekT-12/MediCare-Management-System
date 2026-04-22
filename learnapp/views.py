from django.shortcuts import render, redirect
from learnapp.forms import UserForm, UserProfileForm, UserUpdateForm, UserProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def registration(request):
    registered = False
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = UserProfileForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
    else:
        form1 = UserForm()
        form2 = UserProfileForm()
    context = {'form1': form1, 'form2': form2, 'registered': registered}
    return render(request, "registration.html", context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect("home")
            else:
                return HttpResponse('User not active')
        else:
            return HttpResponse("Please check your credentials")
    return render(request, "login.html", {})


@login_required(login_url="login")
def home(request):
    is_labtech = hasattr(request.user, 'lab_tech')
    context = {'is_labtech': is_labtech}
    if is_labtech:
        context['labtech'] = request.user.lab_tech
    return render(request, "home.html", context)


@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def profile(request):
    from learnapp.models import UserDetails
    from doctors.models import Appointment

    UserDetails.objects.get_or_create(user=request.user)
    is_labtech = hasattr(request.user, 'lab_tech')
    appointments = Appointment.objects.none()

    if not is_labtech:
        appointments = Appointment.objects.filter(user=request.user).select_related('doctor', 'treatment')

    return render(request, "profile.html", {
        'appointments': appointments,
        'is_labtech': is_labtech,
    })


@login_required(login_url="login")
def update(request):
    from learnapp.models import UserDetails
    # FIX 1: get_or_create prevents RelatedObjectDoesNotExist crash
    user_details, _ = UserDetails.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form  = UserUpdateForm(request.POST, instance=request.user)
        form1 = UserProfileUpdateForm(request.POST, request.FILES, instance=user_details)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            profile = form1.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('profile')
        # falls through to re-render with validation errors if invalid
    else:
        form  = UserUpdateForm(instance=request.user)
        form1 = UserProfileUpdateForm(instance=user_details)

    return render(request, "update.html", {'form': form, 'form1': form1})


from labreport.models import Lab_Test

@login_required
def labtech_dashboard(request):
    tests = Lab_Test.objects.all()
    return render(request, 'labreport/dashboard.html', {'tests': tests})

@login_required
def all_tests(request):
    tests = Lab_Test.objects.all()
    return render(request, 'labreport/all_tests.html', {'tests': tests})

@login_required
def pending_tests(request):
    tests = Lab_Test.objects.filter(lab_result='pending')
    return render(request, 'labreport/dashboard.html', {'tests': tests})

def labtechreg(request):
    from labreport.forms import LabTechRegistrationForm
    if request.method == 'POST':
        form = LabTechRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = LabTechRegistrationForm()
    return render(request, 'labtech/labtechreg.html', {'form': form})
