from django.contrib import admin
from .models import UserMedication
from .models import UserVaccine
from .models import UserTrip
from .models import UserProfile
from .models import UserDiet

# Register your models here.
admin.site.register(UserMedication)
admin.site.register(UserVaccine)
admin.site.register(UserTrip)
admin.site.register(UserProfile)
admin.site.register(UserDiet)