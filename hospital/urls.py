from django.urls import path
from .views import home, patient_signup, doctor_signup, signup_success, patient_login, doctor_login

urlpatterns = [
    path('', home, name='home'),
    path('patient_signup/', patient_signup, name='patient_signup'),
    path('doctor_signup/', doctor_signup, name='doctor_signup'),
    path('doctor_login/', doctor_login, name='doctor_login'),
    path('patient_login/', patient_login, name='patient_login'),
    path('signup_success/', signup_success, name='signup_success'),
]