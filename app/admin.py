from django.contrib import admin
from app.models import *
# Register your models here.
class customisedSchool(admin.ModelAdmin):
    list_display=['Sname','Sprincipal','Slocation','email','confirmemail']


admin.site.register(School,customisedSchool)
