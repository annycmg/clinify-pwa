from django.contrib import admin
from .models import UserMedication
from .models import UserVaccine
from .models import UserTrip

# Register your models here.
admin.site.register(UserMedication)
admin.site.register(UserVaccine)
admin.site.register(UserTrip)