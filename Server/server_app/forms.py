from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserMedication
from .models import UserTrip
from .models import UserProfile
from .models import UserVaccine
from .models import UserDiet
from .models import UserAppoint

# SignupForm: formulário de infos básicas
class SignUpForm(UserCreationForm):
    username   = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name  = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    email      = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1  = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2  = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# ProfileForm: extende o SignUpForm com infos específicas
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        widgets = {'profile_blood_prf': forms.Select}
        fields = ['profile_age_prf','profile_loc_prf','profile_weight_prf','profile_height_prf','profile_allergy_prf', 'profile_blood_prf', 'profile_desease_prf','profile_diet_prf','profile_surgery_prf','profile_exerc_prf']
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['profile_age_prf'].widget.attrs.update({'class': 'form-control'})
        self.fields['profile_loc_prf'].widget.attrs.update({'class': 'form-control'})
        self.fields['profile_weight_prf'].widget.attrs.update({'placeholder': 'Kg', 'class': 'form-control'})
        self.fields['profile_height_prf'].widget.attrs.update({'placeholder': 'cm', 'class': 'form-control'})
        self.fields['profile_allergy_prf'].widget.attrs.update({'class': 'form-control'})
        self.fields['profile_desease_prf'].widget.attrs.update({'class': 'form-control'})
        self.fields['profile_diet_prf'].widget.attrs.update({'class': 'form-control'})
        self.fields['profile_surgery_prf'].widget.attrs.update({'class': 'form-control'})
        self.fields['profile_exerc_prf'].widget.attrs.update({'class': 'form-control'}) 

class MedicationForm(ModelForm):
    class Meta:
        model = UserMedication
        fields = ['medication_name_med', 'dosis_name_med', 'init_date_med', 'end_date_med', 'time_med']
    def __init__(self, *args, **kwargs):
        super(MedicationForm, self).__init__(*args, **kwargs)
        self.fields['medication_name_med'].widget.attrs.update({'placeholder': 'Paracetamol', 'class': 'form-control', 'required': ''})
        self.fields['dosis_name_med'].widget.attrs.update({'placeholder': '30 mg/l', 'class': 'form-control', 'required': ''})
        self.fields['init_date_med'].widget.attrs.update({'placeholder': 'YYYY-MM-DD', 'class': 'form-control', 'id': 'datepicker', 'required': ''})
        self.fields['end_date_med'].widget.attrs.update({'placeholder': 'YYYY-MM-DD', 'class': 'form-control', 'id': 'datepicker1', 'required': ''})
        self.fields['time_med'].widget.attrs.update({'placeholder': 'HH:MM:SS', 'class': 'form-control', 'required': ''})


class TripForm(ModelForm):
    class Meta:
        model = UserTrip
        fields = ['trip_country_trp', 'init_date_trp', 'end_date_trp']
    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.fields['trip_country_trp'].widget.attrs.update({'placeholder': 'Argentina; Uruguai;', 'class': 'form-control', 'required': ''})
        self.fields['init_date_trp'].widget.attrs.update({'placeholder': 'AAAA-MM-DD', 'class': 'form-control', 'id': 'datepicker2', 'required': ''})
        self.fields['end_date_trp'].widget.attrs.update({'placeholder': 'AAAA-MM-DD', 'class': 'form-control', 'id': 'datepicker3', 'required': ''})


class VaccineForm(ModelForm):
    class Meta:
        model = UserVaccine
        fields = ['vaccine_name_vac', 'vaccine_date_vac']
    def __init__(self, *args, **kwargs):
        super(VaccineForm, self).__init__(*args, **kwargs)
        self.fields['vaccine_name_vac'].widget.attrs.update({'placeholder': 'Febre Amarela', 'class': 'form-control', 'required': ''})
        self.fields['vaccine_date_vac'].widget.attrs.update({'placeholder': 'AAAA-MM-DD', 'class': 'form-control', 'id': 'datepicker4', 'required': ''})


class DietForm(forms.ModelForm):
    class Meta:
        model = UserDiet
        fields = ['diet_include', 'diet_date_diet', 'meal']
        widgets = {'meal': forms.RadioSelect}
    def __init__(self, *args, **kwargs):
        super(DietForm, self).__init__(*args, **kwargs)
        self.fields['diet_include'].widget.attrs.update({'class': 'form-control', 'required': '', 'aria-label': 'With textarea', 'rows':6})
        self.fields['diet_date_diet'].widget.attrs.update({'placeholder': 'AAAA-MM-DD', 'class': 'form-control', 'id': 'datepicker5', 'required': ''})


class AppointForm(forms.ModelForm):
    class Meta:
        model = UserAppoint
        fields = ['appoint_espec_apt','appoint_date_apt','appoint_time_apt','appoint_nmed_apt','appoint_credenc_apt']
    def __init__(self, *args, **kwargs):
        super(AppointForm, self).__init__(*args, **kwargs)
        self.fields['appoint_espec_apt'].widget.attrs.update({'placeholder': 'Oftalmologista', 'class': 'form-control', 'required': ''})
        self.fields['appoint_date_apt'].widget.attrs.update({'placeholder': 'AAAA-MM-DD', 'class': 'form-control', 'required': '', 'id': 'datepicker6'})
        self.fields['appoint_time_apt'].widget.attrs.update({'placeholder': 'HH:MM:SS', 'class': 'form-control', 'required': ''})
        self.fields['appoint_nmed_apt'].widget.attrs.update({'class': 'form-control', 'required': ''})
        self.fields['appoint_credenc_apt'].widget.attrs.update({'placeholder': 'CRM/CRO/CRP/CRN','class': 'form-control'})