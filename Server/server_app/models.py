from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# ================================ PROFILE MODEL ========================================== #
class UserProfile(models.Model):
    CHOICE = (('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'))  

    user                 = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_age_prf      = models.IntegerField(null=True, blank=True)
    profile_loc_prf      = models.CharField(max_length=150, null=True, blank=True)
    profile_weight_prf   = models.FloatField(null=True, blank=True)
    profile_height_prf   = models.IntegerField(null=True, blank=True)
    profile_allergy_prf  = models.CharField(max_length=200,null=True, blank=True)
    profile_blood_prf    = models.CharField(null=True, max_length=10, default=None, choices=CHOICE, blank=True)
    profile_desease_prf  = models.CharField(max_length=200, null=True, blank=True)
    profile_diet_prf     = models.CharField(max_length=200, null=True, blank=True)
    profile_surgery_prf  = models.CharField(max_length=200, null=True, blank=True)
    profile_exerc_prf    = models.CharField(max_length=200, null=True, blank=True)
    slug                 = models.SlugField(default='slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

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
        return self.user.username
    objects = models.Manager()
# ============================== END MEDICATION MODEL ===================================== #


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
        return self.user.username
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
        return self.user.username
    objects = models.Manager() 
# ============================== END RECENT VACCINE MODEL ======================================= #


# ===================================  DIET MODEL ================================================ #
class UserDiet(models.Model):
    CHOICE = (('Café', 'Café'), ('Almoço', 'Almoço'), ('Jantar', 'Jantar'), ('Snacks', 'Snacks'))  

    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    diet_include    = models.TextField(max_length=500)
    diet_date_diet  = models.DateField()
    meal            = models.CharField(null=False, max_length=10, default=None, choices=CHOICE)
    slug            = models.SlugField(default='slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.meal)
        super(UserDiet, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    objects = models.Manager()
# ======================================= END DIET MODEL =========================================== #


# ===================================== APPOINTMENTS MODEL ========================================= #
class UserAppoint(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    appoint_espec_apt   = models.CharField(max_length=50)
    appoint_date_apt    = models.DateField()
    appoint_time_apt    = models.TimeField()
    appoint_nmed_apt    = models.CharField(max_length=50)
    appoint_credenc_apt = models.CharField(max_length=20)
    slug                = models.SlugField(default='slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.appoint_espec_apt)
        super(UserAppoint, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    objects = models.Manager()
# ==================================== END APPOINTMENTS MODEL ======================================= #
