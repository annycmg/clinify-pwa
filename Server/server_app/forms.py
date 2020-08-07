from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserMedication
from .models import UserTrip
from .models import UserProfile
from .models import UserVaccine
from .models import UserDiet

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
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['profile_age_prf'].widget.attrs.update({'class': 'form-control', 'required': ''})
        self.fields['profile_loc_prf'].widget.attrs.update({'class': 'form-control', 'required': ''})
        self.fields['profile_weight_prf'].widget.attrs.update({'placeholder': 'Kg', 'class': 'form-control', 'required': ''})
        self.fields['profile_height_prf'].widget.attrs.update({'placeholder': 'cm', 'class': 'form-control', 'required': ''})
        self.fields['profile_allergy_prf'].widget.attrs.update({'class': 'form-control', 'required': ''})
        self.fields['profile_desease_prf'].widget.attrs.update({'class': 'form-control', 'required': ''})
        self.fields['profile_diet_prf'].widget.attrs.update({'class': 'form-control', 'required': ''})
        self.fields['profile_surgery_prf'].widget.attrs.update({'class': 'form-control', 'required': ''})
        self.fields['profile_exerc_prf'].widget.attrs.update({'class': 'form-control', 'required': ''})


class MedicationForm(ModelForm):
    class Meta:
        model = UserMedication
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(MedicationForm, self).__init__(*args, **kwargs)
        self.fields['medication_name_med'].widget.attrs.update({'placeholder': 'Paracetamol', 'class': 'form-control', 'required': ''})
        self.fields['dosis_name_med'].widget.attrs.update({'placeholder': '30 mg/l', 'class': 'form-control', 'required': ''})
        self.fields['init_date_med'].widget.attrs.update({'placeholder': 'YYYY-MM-DD', 'class': 'form-control', 'required': ''})
        self.fields['end_date_med'].widget.attrs.update({'placeholder': 'YYYY-MM-DD', 'class': 'form-control', 'required': ''})
        self.fields['time_med'].widget.attrs.update({'placeholder': 'HH:MM:SS', 'class': 'form-control', 'required': ''})


class TripForm(ModelForm):
    class Meta:
        model = UserTrip
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.fields['trip_country_trp'].widget.attrs.update({'placeholder': 'Argentina; Uruguai;', 'class': 'form-control', 'required': ''})
        self.fields['init_date_trp'].widget.attrs.update({'placeholder': 'AAAA-MM-DD', 'class': 'form-control', 'required': ''})
        self.fields['end_date_trp'].widget.attrs.update({'placeholder': 'AAAA-MM-DD', 'class': 'form-control', 'required': ''})


class VaccineForm(ModelForm):
    class Meta:
        model = UserVaccine
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(VaccineForm, self).__init__(*args, **kwargs)
        self.fields['vaccine_name_vac'].widget.attrs.update({'placeholder': 'Febre Amarela', 'class': 'form-control', 'required': ''})
        self.fields['vaccine_date_vac'].widget.attrs.update({'placeholder': 'AAAA-MM-DD', 'class': 'form-control', 'required': ''})


class DietForm(ModelForm):
    class Meta:
        model = UserDiet
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(DietForm, self).__init__(*args, **kwargs)
        self.fields['diet_include'].widget.attrs.update({'class': 'form-control', 'required': '', 'aria-label': 'With textarea'})
        