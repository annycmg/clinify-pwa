from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# ================================ PROFILE MODEL ========================================== #
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
# ============================ END PROFILE MODEL ========================================== #


# ================================ MEDICATION MODEL ======================================= #
class UserMedication(models.Model):
    user                 = models.ForeignKey(User, on_delete=models.CASCADE)
    medication_name_med  = models.CharField(max_length=200)
    dosis_name_med       = models.CharField(max_length=30)
    init_date_med        = models.DateField()
    end_date_med         = models.DateField()
    time_med             = models.TimeField()
    slug                 = models.SlugField(default='slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.medication_name_med)
        super(UserMedication, self).save(*args, **kwargs)

    def __str__(self):
        return self.medication_name_med
    objects = models.Manager()
# ================================ END MEDICATION MODEL ================================ #


# ================================ RECENT TRIPS MODEL ======================================= #
class UserTrip(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_country_trp = models.CharField(max_length=300)
    init_date_trp    = models.DateField()
    end_date_trp     = models.DateField()
    slug             = models.SlugField(default='slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.trip_country_trp)
        super(UserTrip, self).save(*args, **kwargs)

    def __str__(self):
        return self.trip_country_trp
    objects = models.Manager()
# ================================ END RECENT TRIPS MODEL ======================================= #


# ================================ RECENT VACCINE MODEL ========================================= #
class UserVaccine(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    vaccine_name_vac = models.CharField(max_length=200)
    vaccine_date_vac = models.DateField()
    slug             = models.SlugField(default='slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.vaccine_name_vac)
        super(UserVaccine, self).save(*args, **kwargs)

    def __str__(self):
        return self.vaccine_name_vac
    objects = models.Manager() 
# ============================== END RECENT VACCINE MODEL ======================================= #


class UserDiet(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    diet_include   = models.TextField(max_length=500)
    diet_date_diet = models.DateField()
    slug           = models.SlugField(default='slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.diet_include)
        super(UserDiet, self).save(*args, **kwargs)

    def __str__(self):
        return self.diet_include
    objects = models.Manager()
