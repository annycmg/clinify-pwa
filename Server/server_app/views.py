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
def home(request):
    return render(request, 'home.html')

def forgpassword(request):
    return render(request, 'forgpassword.html')

@login_required
def medication(request):
    return render(request, 'medication.html')

@login_required
def diet(request):
    return render(request, 'diet.html')

@login_required
def exercise(request):
    return render(request, 'exercise.html')
 
@login_required
def recenttrips(request):
    return render(request, 'recenttrips.html')

@login_required
def recentvaccine(request):
    return render(request, 'recentvaccine.html')

@login_required
def appointment(request):
    return render(request, 'appointment.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def editprofile(request):
    return render(request, 'editprofile.html')

def offline(request):
    return render(request, 'offline.html')

def base(request):
    return render(request, 'base.html')