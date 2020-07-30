from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# UserProfile: extensão das infos básicas de User
class UserProfile(models.Model):
    user                 = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_age_prf      = models.IntegerField()
    profile_loc_prf      = models.CharField(max_length=150)
    profile_weight_prf   = models.FloatField()
    profile_height_prf   = models.IntegerField()
    profile_allergy_prf  = models.CharField(max_length=200)
    profile_desease_prf  = models.CharField(max_length=200)
    profile_diet_prf     = models.CharField(max_length=200)
    profile_surgery_prf  = models.CharField(max_length=200)
    profile_exerc_prf    = models.CharField(max_length=200)
    def __str__(self):
        return self.user.username

User = get_user_model()
class UserMedication(models.Model):
    user                 = models.ForeignKey(User, on_delete=models.CASCADE)
    medication_name_med  = models.CharField(max_length=200)
    dosis_name_med       = models.CharField(max_length=30)
    init_date_med        = models.DateField()
    end_date_med         = models.DateField()
    time_med             = models.TimeField()
    def __str__(self):
        return self.user.username

class UserVaccine(models.Model):
    vaccine_name_vac = models.CharField(max_length=200)
    vaccine_date_vac = models.DateField()

class UserTrip(models.Model):
    trip_country_trp = models.CharField(max_length=300)
    init_date_trp    = models.DateField()
    end_date_trp     = models.DateField()

class UserDiet(models.Model):
    diet_include = models.TextField(max_length=500)
