from django.shortcuts import render, redirect
from .forms import PatientSignupForm, DoctorSignupForm, PatientLoginForm, DoctorLoginForm
from pymongo import MongoClient

client = MongoClient('mongodb+srv://srawan_meesala:db_user@cluster0.kcqiur4.mongodb.net/?retryWrites=true&w=majority')
db = client['accounts']

def home(request):
    return render(request, 'hospital/home.html')

def patient_login(request):
    patients_collection = db['doctors']
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            patient = patients_collection.find_one({'username': username})
            if patient['password'] == form.cleaned_data['password']:
                return render(request, 'hospital/patient_dashboard.html', {'user': patient})
            else:
                return render(request, 'hospital/patient_login.html', {'form': form})
    else:
        form = PatientLoginForm()
        return render(request, 'hospital/patient_login.html', {'form': form})

def patient_signup(request):
    patients_collection = db['patients']
    if request.method == 'POST':
        form = PatientSignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                if 'pfp' in form.cleaned_data: print(form.cleaned_data['pfp'])
                else: print('Not found')
                patient_data = {
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'email': form.cleaned_data['email'],
                    'username': form.cleaned_data['username'],
                    'phone_number': form.cleaned_data['phone_number'],
                    'address': form.cleaned_data['address'],
                    'city': form.cleaned_data['city'],
                    'state': form.cleaned_data['state'],
                    'password': form.cleaned_data['password']
                }
                patients_collection.insert_one(patient_data)
                print(patient_data)
                return render(request, 'hospital/patient_dashboard.html', {'user': patient_data})

        else:
            form = PatientSignupForm()
    else:
        form = PatientSignupForm()
    return render(request, 'hospital/patient_signup.html', {'form': form})

def doctor_login(request):
    doctors_collection = db['doctors']
    if request.method == 'POST':
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            doc = doctors_collection.find_one({'username': username})
            if doc['password'] == form.cleaned_data['password']:
                return render(request, 'hospital/doctor_dashboard.html', {'user': doc})
            else:
                return render(request, 'hospital/doctor_login.html', {'form': form})
    else:
        form = DoctorLoginForm()
        return render(request, 'hospital/doctor_login.html', {'form': form})

def doctor_signup(request):
    doctors_collection = db['doctors']
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                if 'pfp' in form.cleaned_data: print(form.cleaned_data['pfp'])
                else: print('Not found')
                doctor_data = {
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'email': form.cleaned_data['email'],
                    'username': form.cleaned_data['username'],
                    'phone_number': form.cleaned_data['phone_number'],
                    'address': form.cleaned_data['address'],
                    'city': form.cleaned_data['city'],
                    'state': form.cleaned_data['state'],
                    'password': form.cleaned_data['password']
                }
                doctors_collection.insert_one(doctor_data)
                return render(request, 'hospital/doctor_dashboard.html', {'user': doctor_data})
        else:
            form = DoctorSignupForm()
    else:
        form = DoctorSignupForm()
    return render(request, 'hospital/doctor_signup.html', {'form': form})

def signup_success(request):
    return render(request, 'hospital/signup_success.html')