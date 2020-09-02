import calendar
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime, date
from django.utils.safestring import mark_safe
from datetime import timedelta
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import pdfkit

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import SignUpForm
from .forms import ProfileForm
from .forms import MedicationForm
from .forms import TripForm
from .forms import VaccineForm
from .forms import DietForm
from .forms import AppointForm

from .models import UserMedication
from .models import UserTrip
from .models import UserVaccine
from .models import UserDiet
from .models import UserProfile
from .models import UserAppoint

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def logoutUser(request):
    print("Log out com sucesso")
    return redirect('intro')

def offline(request):
    return render(request, 'offline.html')

def base(request):
    return render(request, 'base.html')

# ========================================== DO!!! EXERCISE CRUD ====================================== #
@login_required
def exercise(request):
    return render(request, 'exercise.html')
# ====================================== DO!!! END EXERCISE CRUD ======================================== #


# =================================== LOGIN & PASSWORD AUTHETICATION ================================== #
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
# ==================================== END AUTHETICATION ============================================== #


# ========================================= SIGNUP ==================================================== #
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


# ======================================== TRIPS CRUD ============================================= #
@method_decorator(login_required(login_url="intro"), name='dispatch')
class TripListView(ListView): ### RETRIEVE
    template_name="trip_list.html"
    model = UserTrip
    context_object_name = 'trip'
    def get_context_data(self, **kwargs): 
        context = super(TripListView, self).get_context_data(**kwargs)
        return context
    def get_queryset(self):
        queryset = super(TripListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

@method_decorator(login_required(login_url="intro"), name='dispatch')
class TripDetailView(DetailView): ### RETRIEVE
    template_name = "trip_detail.html"
    model = UserTrip
    context_object_name = 'single_trip'
    def get_context_data(self, **kwargs):
        context = super(TripDetailView, self).get_context_data(**kwargs)
        return context

@method_decorator(login_required(login_url="intro"), name='dispatch')
class TripCreateView(CreateView): ### CREATE
    template_name = "recenttrips.html"
    model = UserTrip
    form_class = TripForm
    def get_success_url(self):
        return reverse("temp:trip_detail", kwargs={'pk':self.object.pk, 'slug':self.object.slug})
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        print("trip inserted and saved")
        return super(TripCreateView, self).form_valid(form)

@method_decorator(login_required(login_url="intro"), name='dispatch')
class TripUpdateView(UpdateView):  ### UPDATE
    template_name = "recenttrips.html"
    model = UserTrip
    form_class = TripForm
    def get_success_url(self):
        return reverse("temp:trip_detail", kwargs={'pk':self.object.pk, 'slug':self.object.slug})
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        print("trip updated and saved")
        return super(TripUpdateView, self).form_valid(form)

@method_decorator(login_required(login_url="intro"), name='dispatch')
class TripDeleteView(DeleteView): ### DELETE
    model = UserTrip
    success_url = 'temp:trip_list'
    template_name = 'trip_delete.html'
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            print("trip safely deleted")
            return HttpResponseRedirect(reverse(self.success_url))
        else:
            return HttpResponseRedirect(self.success_url)
# ======================================== END TRIPS CRUD ========================================== #

# ========================================= VACCINE CRUD ============================================ #
@method_decorator(login_required(login_url="intro"), name='dispatch')
class VaccineListView(ListView): ### RETRIEVE
    template_name="vaccine_list.html"
    model = UserVaccine
    context_object_name = 'vac'
    def get_context_data(self, **kwargs): 
        context = super(VaccineListView, self).get_context_data(**kwargs)
        return context
    def get_queryset(self):
        queryset = super(VaccineListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

@method_decorator(login_required(login_url="intro"), name='dispatch')
class VaccineDetailView(DetailView): ### RETRIEVE
    template_name = "vaccine_detail.html"
    model = UserVaccine
    context_object_name = 'single_vaccine'
    def get_context_data(self, **kwargs):
        context = super(VaccineDetailView, self).get_context_data(**kwargs)
        return context

@method_decorator(login_required(login_url="intro"), name='dispatch')
class VaccineCreateView(CreateView): ### CREATE
    template_name = "recentvaccine.html"
    model = UserVaccine
    form_class = VaccineForm
    def get_success_url(self):
        return reverse("temp:vaccine_detail", kwargs={'pk':self.object.pk, 'slug':self.object.slug})
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        print("vaccine inserted and saved")
        return super(VaccineCreateView, self).form_valid(form)

@method_decorator(login_required(login_url="intro"), name='dispatch')
class VaccineUpdateView(UpdateView):  ### UPDATE
    template_name = "recentvaccine.html"
    model = UserVaccine
    form_class = VaccineForm
    def get_success_url(self):
        return reverse("temp:vaccine_detail", kwargs={'pk':self.object.pk, 'slug':self.object.slug})
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        print("vaccine updated and saved")
        return super(VaccineUpdateView, self).form_valid(form)

@method_decorator(login_required(login_url="intro"), name='dispatch')
class VaccineDeleteView(DeleteView): ### DELETE
    model = UserVaccine
    success_url = 'temp:vaccine_list'
    template_name = 'vaccine_delete.html'
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            print("vaccine safely deleted")
            return HttpResponseRedirect(reverse(self.success_url))
        else:
            return HttpResponseRedirect(self.success_url)

# ======================================== END VACCINE CRUD ========================================= #


# =========================================== DIET CRUD ============================================= #
@method_decorator(login_required(login_url="intro"), name='dispatch')
class DietListView(ListView): ### RETRIEVE
    template_name="diet_list.html"
    model = UserDiet
    context_object_name = 'diet'
    def get_context_data(self, **kwargs): 
        context = super(DietListView, self).get_context_data(**kwargs)
        return context
    def get_queryset(self):
        queryset = super(DietListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

@method_decorator(login_required(login_url="intro"), name='dispatch')
class DietDetailView(DetailView): ### RETRIEVE
    template_name = "diet_detail.html"
    model = UserDiet
    context_object_name = 'single_diet'
    def get_context_data(self, **kwargs):
        context = super(DietDetailView, self).get_context_data(**kwargs)
        return context

@method_decorator(login_required(login_url="intro"), name='dispatch')
class DietCreateView(CreateView): ### CREATE
    template_name = "diet.html"
    model = UserDiet
    form_class = DietForm
    def get_success_url(self):
        return reverse("temp:diet_detail", kwargs={'pk':self.object.pk, 'slug':self.object.slug})
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        print("meal inserted and saved")
        return super(DietCreateView, self).form_valid(form)

@method_decorator(login_required(login_url="intro"), name='dispatch')
class DietUpdateView(UpdateView):  ### UPDATE
    template_name = "diet.html"
    model = UserDiet
    form_class = DietForm
    def get_success_url(self):
        return reverse("temp:diet_detail", kwargs={'pk':self.object.pk, 'slug':self.object.slug})
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        print("meal updated and saved")
        return super(DietUpdateView, self).form_valid(form)

@method_decorator(login_required(login_url="intro"), name='dispatch')
class DietDeleteView(DeleteView): ### DELETE
    model = UserDiet
    success_url = 'temp:diet_list'
    template_name = 'diet_delete.html'
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            print("meal safely deleted")
            return HttpResponseRedirect(reverse(self.success_url))
        else:
            return HttpResponseRedirect(self.success_url)
# ========================================== END DIET CRUD =========================================== #


# ======================================== PROFILE DISPLAY/UPDATE ====================================== #
@method_decorator(login_required(login_url="intro"), name='dispatch')
class ProfileListView(ListView):
    template_name = 'profile.html'
    model = UserMedication
    context_object_name = 'med'   

    def get_queryset(self):
        queryset = super(ProfileListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset 

    def get_context_data(self, **kwargs):
        kwargs['userprof'] = UserProfile.objects.get(user=self.request.user)
        kwargs['trip'] = UserTrip.objects.filter(user=self.request.user)
        kwargs['vac'] = UserVaccine.objects.filter(user=self.request.user)
        kwargs['appoint'] = UserAppoint.objects.filter(user=self.request.user)
        kwargs['diet'] = UserDiet.objects.filter(user=self.request.user)
        return super(ProfileListView, self).get_context_data(**kwargs)

def render_to_pdf(request):
    # Use False instead of output path to save pdf to a variable
    pdf = pdfkit.from_url('https://github.com/annycmg/clinify-pwa', False) # Change for clinify website page
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="progresso.pdf"'
    return response

@method_decorator(login_required(login_url="intro"), name='dispatch')
class ProfileUpdateView(UpdateView):  ### UPDATE
    template_name = "editprofile.html"
    model = UserProfile
    form_class = ProfileForm
    def get_success_url(self):
        return reverse("temp:profile")
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        print("profile updated and saved")
        return super(ProfileUpdateView, self).form_valid(form)
# ===================================== END PROFILE DISPLAY/UPDATE ===================================== #


# ================================== DO!!! GOOGLE CALENDAR APPOINTMENTS ================================== #
@method_decorator(login_required(login_url="intro"), name='dispatch')
class AppointCalendarListView(ListView): ### RETRIEVE
    template_name="appoint_calendar.html"
    model = UserAppoint
    context_object_name = 'appoint'
    def get_context_data(self, **kwargs): 
        context = super(AppointCalendarListView, self).get_context_data(**kwargs)
        return context
    def get_queryset(self):
        queryset = super(AppointCalendarListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

@method_decorator(login_required(login_url="intro"), name='dispatch')
class AppointDetailView(DetailView): ### RETRIEVE
    template_name = "appointment_detail.html"
    model = UserAppoint
    context_object_name = 'single_appoint'
    def get_context_data(self, **kwargs):
        context = super(AppointDetailView, self).get_context_data(**kwargs)
        return context

@method_decorator(login_required(login_url="intro"), name='dispatch')
class AppointCreateView(CreateView): ### CREATE
    template_name = "appointment.html"
    model = UserAppoint
    form_class = AppointForm
    def get_success_url(self):
        return reverse("temp:appoint_detail", kwargs={'pk':self.object.pk, 'slug':self.object.slug})
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        print("appointment inserted and saved")
        return super(AppointCreateView, self).form_valid(form)

@method_decorator(login_required(login_url="intro"), name='dispatch')
class AppointUpdateView(UpdateView):  ### UPDATE
    template_name = "appointment.html"
    model = UserAppoint
    form_class = AppointForm
    def get_success_url(self):
        return reverse("temp:appoint_detail", kwargs={'pk':self.object.pk, 'slug':self.object.slug})
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        print("appointment updated and saved")
        return super(AppointUpdateView, self).form_valid(form)

@method_decorator(login_required(login_url="intro"), name='dispatch')
class AppointDeleteView(DeleteView): ### DELETE
    model = UserAppoint
    success_url = 'temp:appoint_calendar'
    template_name = 'appointment_delete.html'
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            print("appointment safely deleted")
            return HttpResponseRedirect(reverse(self.success_url))
        else:
            return HttpResponseRedirect(self.success_url)
# ================================= END GOOGLE CALENDAR APPOINTMENTS ================================== #














# ========================================== DO!!! PDF EXPORTER ======================================== #


# ========================================== DO!!! BASIC PWA ========================================== #


# ======================================= DO!!! DEPLOY ON WEB ========================================== #
