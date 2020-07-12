from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

# Create your views here.
def intro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username E/OU senha incorretos.')
    return render(request, 'intro.html')

def logoutUser(request):
    logout(request)
    return redirect('intro')


def forgpassword(request):
    return render(request, 'forgpassword.html')

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() 
            user = form.cleaned_data.get('first_name') 
            messages.success(request, user + ", a sua conta foi criada com sucesso! Agora você já pode fazer seu Login.")
            return redirect('intro')
    return render(request, 'signup.html', {'form':form})

@login_required(login_url='intro')
def home(request):
    return render(request, 'home.html')

def medication(request):
    return render(request, 'medication.html')

def diet(request):
    return render(request, 'diet.html')

def exercise(request):
    return render(request, 'exercise.html')
 
def recenttrips(request):
    return render(request, 'recenttrips.html')

def recentvaccine(request):
    return render(request, 'recentvaccine.html')

def appointment(request):
    return render(request, 'appointment.html')

def profile(request):
    return render(request, 'profile.html')

def editprofile(request):
    return render(request, 'editprofile.html')

def offline(request):
    return render(request, 'offline.html')

def base(request):
    return render(request, 'base.html')