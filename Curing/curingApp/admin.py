from django.contrib import admin
from .models import Pole,CuringSchedule

# Register your models here.
class Adminpole(admin.ModelAdmin):
    list_display = ['project_name','pole_constructed']
admin.site.register(Pole,Adminpole)

class AdminCuringSchedule(admin.ModelAdmin):
    list_display = ['pole','start_date']
admin.site.register(CuringSchedule,AdminCuringSchedule)