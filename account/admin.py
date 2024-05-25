from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "KARINI"

admin.site.register(UserCourse)
admin.site.register(Matiere)
admin.site.register(Bacalorea)
admin.site.register(Etudiante)
admin.site.register(Enseignant)
admin.site.register(Cour)
