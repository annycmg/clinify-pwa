from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import SignUpForm
from .forms import ProfileForm
from .forms import MedicationForm
from .forms import TripForm
from .forms import VaccineForm
from .forms import DietForm

from .models import UserMedication
from .models import UserTrip
from .models import UserVaccine
from .models import UserDiet

# import datetime
# import pickle
# import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request


# =============================== LOGIN & PASSWORD AUTHETICATION ================================== #
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
# ================================ END AUTHETICATION ============================================== #


# ====================================== SIGNUP ==================================================== #
# signup: formulário com infos básicas e infos de perfil para cadastro
def signup(request):
    if request.method == 'POST':
        form_signup = SignUpForm(request.POST)
        form_profile = ProfileForm(request.POST)
        if form_signup.is_valid() and form_profile.is_valid():
            user = form_signup.save() 
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()
            usern = form_signup.cleaned_data.get('username') 
            messages.success(request, usern + ", a sua conta foi criada com sucesso! Agora você já pode fazer seu Login.")
            print('Sign up com sucesso')
            return redirect('intro')
        else:
            print("Something went wrong :(")
            print(form_profile.errors, form_signup.errors)
    else:
        form_signup = SignUpForm()
        form_profile = ProfileForm()
    return render(request, 'signup.html', {'form_signup':form_signup, 'form_profile':form_profile})
# ======================================== END SIGNUP =============================================== #


# ======================================= MEDICATION CRUD =========================================== #
@method_decorator(login_required(login_url="intro"), name='dispatch')
class MedicationListView(ListView): ### RETRIEVE
    template_name="medication_list.html"
    model = UserMedication
    context_object_name = 'med'
    def get_context_data(self, **kwargs): 
        context = super(MedicationListView, self).get_context_data(**kwargs)
        return context
    def get_queryset(self):
        queryset = super(MedicationListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

@method_decorator(login_required(login_url="intro"), name='dispatch')
class MedicationDetailView(DetailView): ### RETRIEVE
    template_name = "medication_detail.html"
    model = UserMedication
    context_object_name = 'single'
    def get_context_data(self, **kwargs):
        context = super(MedicationDetailView, self).get_context_data(**kwargs)
        return context

@method_decorator(login_required(login_url="intro"), name='dispatch')
class MedicationCreateView(CreateView): ### CREATE
    template_name = "medication.html"
    model = UserMedication
    form_class = MedicationForm
    def get_success_url(self):
        return reverse("temp:medication_detail", kwargs={'pk':self.object.pk, 'slug':self.object.slug})
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        print("medication inserted and saved")
        return super(MedicationCreateView, self).form_valid(form)

@method_decorator(login_required(login_url="intro"), name='dispatch')
class MedicationUpdateView(UpdateView):  ### UPDATE
    template_name = "medication.html"
    model = UserMedication
    form_class = MedicationForm
    def get_success_url(self):
        return reverse("temp:medication_detail", kwargs={'pk':self.object.pk, 'slug':self.object.slug})
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        print("medication updated and saved")
        return super(MedicationUpdateView, self).form_valid(form)
    
@method_decorator(login_required(login_url="intro"), name='dispatch')
class MedicationDeleteView(DeleteView): ### DELETE
    model = UserMedication
    success_url = 'temp:medication_list'
    template_name = 'delete_item.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            print("medication safely deleted")
            return HttpResponseRedirect(reverse(self.success_url))
        else:
            return HttpResponseRedirect(self.success_url)

# ==================================== END MEDICATION CRUD ======================================= #



# trips: retorna a lista das últimas viagens do usuário, vindos do sqlite
@login_required
def recenttrips(request):
    form_trip = TripForm()
    trip = UserTrip.objects.all()
    context = {'form_trip':form_trip, 'trip':trip}
    return render(request, 'recenttrips.html', context)


# vaccines: retorna a lista das últimas vacinas do usuário, vindos do sqlite
@login_required
def recentvaccine(request):
    form_vac = VaccineForm()
    vac = UserVaccine.objects.all()
    context = {'form_vac':form_vac, 'vac':vac}
    return render(request, 'recentvaccine.html', context)


@login_required
def diet(request):
    form_diet = DietForm()
    diet = UserDiet.objects.all()
    context = {'form_diet':form_diet, 'diet':diet}
    return render(request, 'diet.html', context)




@login_required
def editprofile(request):
    return render(request, 'editprofile.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def logoutUser(request):
    print("Log out com sucesso")
    return redirect('intro')

@login_required
def profile(request):
    return render(request, 'profile.html')

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