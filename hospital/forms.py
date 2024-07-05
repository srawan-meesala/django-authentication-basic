from django import forms

class PatientSignupForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    pfp = forms.ImageField(required=False)
    address = forms.CharField(max_length=150)
    city = forms.CharField(max_length=150)
    state = forms.CharField(max_length=150)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)

class DoctorSignupForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    pfp = forms.ImageField(required=False)
    address = forms.CharField(max_length=150)
    city = forms.CharField(max_length=150)
    state = forms.CharField(max_length=150)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)

class PatientLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

class DoctorLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)