from django.db import models

# Create your models here.
class UserMedication(models.Model):
    medication_name_med = models.CharField(max_length=200)
    dosis_name_med = models.CharField(max_length=30)
    init_date_med = models.DateField()
    end_date_med = models.DateField()
    time_med = models.TimeField()

class UserVaccine(models.Model):
    vaccine_name_vac = models.CharField(max_length=200)
    vaccine_date_vac = models.DateField()

class UserTrip(models.Model):
    trip_country_trp = models.CharField(max_length=300)
    init_date_trp = models.DateField()
    end_date_trp = models.DateField()