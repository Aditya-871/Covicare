from django.contrib import admin
from .models import Hospital,Patient,Vaccine,Bed,Oxygen

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(Vaccine)
admin.site.register(Oxygen)
admin.site.register(Bed)
