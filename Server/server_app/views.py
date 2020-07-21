from __future__ import print_function

from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm
from .forms import MedicationForm
from .forms import VaccineForm
from .forms import TripForm
from .forms import ProfileForm
from .forms import DietForm

import datetime
import pickle
import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

def intro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('Log in com sucesso')
            return redirect('home')
        else:
            messages.info(request, 'Username E/OU senha incorretos.')
    return render(request, 'intro.html')

@login_required
def logoutUser(request):
    print("Log out com sucesso")
    return redirect('intro')

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() 
            user = form.cleaned_data.get('first_name') 
            messages.success(request, user + ", a sua conta foi criada com sucesso! Agora você já pode fazer seu Login.")
            print('Sign up com sucesso')
            return redirect('intro')
    return render(request, 'signup.html', {'form':form})

@login_required
def medication(request):
    form = MedicationForm()
    if request.method == "POST":
        form = MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('temp:medication')
    return render(request, 'medication.html', {'form': form})

@login_required
def recentvaccine(request):
    form = VaccineForm()
    if request.method == "POST":
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('temp:recentvaccine')
    return render(request, 'recentvaccine.html', {'form': form})

@login_required
def recenttrips(request):
    form = TripForm()
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('temp:recenttrips')
    return render(request, 'recenttrips.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def editprofile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('temp:profile')
    return render(request, 'editprofile.html', {'form':form})

@login_required
def diet(request):
    form = DietForm()
    if request.method == "POST":
        form = DietForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('temp:diet')
    return render(request, 'diet.html')

@login_required
def exercise(request):
    return render(request, 'exercise.html')

@login_required
def appointment(request):

    # SCOPES = ['https://www.googleapis.com/auth/calendar']
    # creds = None
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file('server_app/client_secret.json', SCOPES)
    #         creds = flow.run_local_server(port=0)
    # service = build('calendar', 'v3', credentials=creds)

    return render(request, 'appointment.html')



def forgpassword(request):
    return render(request, 'forgpassword.html')

def offline(request):
    return render(request, 'offline.html')

def base(request):
    return render(request, 'base.html')