# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm, PatientForm  # Import PatientForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def home(request):
    return render(request, 'home.html')

@login_required  # Ensure the user is logged in before accessing this view
def successfully_registered(request):
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)  # Initialize with POST data
        if patient_form.is_valid():
            patient_form.save()  # Save the patient form data
            return redirect('successfully_registered')  # Redirect or show success message
            
    else:
        patient_form = PatientForm()  # Create a new form instance for GET request

    return render(request, 'users/successfully_registered.html', {'patient_form': patient_form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')
            dob = form.cleaned_data.get('dob')
            # Saving phone_number and dob to the UserProfile model
            profile = UserProfile(user=user, phone_number=phone_number, dob=dob)
            profile.save()
            login(request, user)
            return redirect('successfully_registered')
    
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required  # Ensure the user is logged in before accessing this view
def successfully_logged_in(request):
    return render(request, 'users/successfully_logged_in.html')

def login_view(request):  # Don't name "login" because Django already has a built-in log in function
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('successfully_logged_in')  # Redirect on successful login
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
