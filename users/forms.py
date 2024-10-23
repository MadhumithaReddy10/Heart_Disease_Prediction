from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Patient

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    dob = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900,2024)))

    class Meta:
        model = User
        fields = ['username', 'email','phone_number','dob', 'password1', 'password2']

class PatientForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(required=True)
    phn_number = forms.CharField(max_length=15, required=True)
    blood_pressure = forms.CharField(max_length=10) 
    sugar_levels = forms.CharField(max_length=10) 

    class Meta:
        model = Patient 
        fields = ['name', 'age', 'phn_number', 'blood_pressure', 'sugar_levels']