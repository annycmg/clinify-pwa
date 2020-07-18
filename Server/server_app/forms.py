from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from server_app.models import UserVaccine
from server_app.models import UserMedication
from server_app.models import UserTrip

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = '__all__'

class TripForm(ModelForm):
    class Meta:
        model = UserTrip
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.fields['trip_country_trp'].widget.attrs.update({'placeholder': 'Argentina, Uruguai', 'class': 'form-control', 'required': ''})
        self.fields['init_date_trp'].widget.attrs.update({'placeholder': 'AAAA-MM-DD', 'class': 'form-control', 'required': ''})
        self.fields['end_date_trp'].widget.attrs.update({'placeholder': 'AAAA-MM-DD', 'class': 'form-control', 'required': ''})


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

class VaccineForm(ModelForm):
    class Meta:
        model = UserVaccine
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(VaccineForm, self).__init__(*args, **kwargs)
        self.fields['vaccine_name_vac'].widget.attrs.update({'placeholder': 'Febre Amarela', 'class': 'form-control', 'required': ''})
        self.fields['vaccine_date_vac'].widget.attrs.update({'placeholder': 'AAAA-MM-DD', 'class': 'form-control', 'required': ''})

