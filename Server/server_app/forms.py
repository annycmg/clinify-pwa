from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserMedication



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

class MedicationForm(ModelForm):
    class Meta:
        model = UserMedication
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MedicationForm, self).__init__(*args, **kwargs)
        self.fields['medication_name_med'].widget.attrs.update({'placeholder': 'Paracetamol', 'class': 'form-control', 'required': ''})
        self.fields['dosis_name_med'].widget.attrs.update({'placeholder': '30 mg/l', 'class': 'form-control', 'required': ''})
        self.fields['init_date_med'].widget.attrs.update({'placeholder': 'MM-DD-YYYY', 'class': 'form-control', 'required': ''})
        self.fields['end_date_med'].widget.attrs.update({'placeholder': 'MM-DD-YYYY', 'class': 'form-control', 'required': ''})
        self.fields['time_med'].widget.attrs.update({'placeholder': 'HH:MM', 'class': 'form-control', 'required': ''})
