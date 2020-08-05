from django.db import models
from django.contrib.auth.models import User

# UserProfile: extensão das infos básicas do User
class UserProfile(models.Model):
    user                 = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
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


class UserMedication(models.Model):
    user                 = models.ForeignKey(User, on_delete=models.CASCADE)
    medication_name_med  = models.CharField(max_length=200)
    dosis_name_med       = models.CharField(max_length=30)
    init_date_med        = models.DateField()
    end_date_med         = models.DateField()
    time_med             = models.TimeField()
    def __str__(self):
        return self.medication_name_med
    objects = models.Manager()



class UserTrip(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_country_trp = models.CharField(max_length=300)
    init_date_trp    = models.DateField()
    end_date_trp     = models.DateField()
    def __str__(self):
        return self.trip_country_trp
    objects = models.Manager()


class UserVaccine(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    vaccine_name_vac = models.CharField(max_length=200)
    vaccine_date_vac = models.DateField()
    def __str__(self):
        return self.vaccine_name_vac
    objects = models.Manager() 


class UserDiet(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    diet_include = models.TextField(max_length=500)
    def __str__(self):
        return self.diet_include
    objects = models.Manager()
