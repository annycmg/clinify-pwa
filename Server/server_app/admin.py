from django.contrib import admin
from .models import UserMedication
from .models import UserTrip
from .models import UserProfile
from .models import UserVaccine
from .models import UserDiet

# Register your models here.
class AdminMedication(admin.ModelAdmin):
    list_display = ['user', 'medication_name_med', 'dosis_name_med', 'init_date_med', 'end_date_med', 'time_med']
    class Meta:
        model = UserMedication

class AdminTrip(admin.ModelAdmin):
    list_display = ['user', 'trip_country_trp', 'init_date_trp', 'end_date_trp']
    class Meta:
        model = UserTrip

class AdminVaccine(admin.ModelAdmin):
    list_display = ['user', 'vaccine_name_vac', 'vaccine_date_vac']
    class Meta:
        model = UserVaccine

class AdminDiet(admin.ModelAdmin):
    list_display = ['user', 'meal', 'diet_include', 'diet_date_diet']
    class Meta:
        model = UserDiet

admin.site.register(UserMedication, AdminMedication)
admin.site.register(UserTrip, AdminTrip)
admin.site.register(UserVaccine, AdminVaccine)
admin.site.register(UserDiet, AdminDiet)
admin.site.register(UserProfile)
