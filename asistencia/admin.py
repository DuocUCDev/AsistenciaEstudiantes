from django.contrib import admin
from .models import Asistencia, Seccion, Estudiante, Curso

# Register your models here.
admin.site.register(Asistencia)
admin.site.register(Seccion)
admin.site.register(Estudiante)
admin.site.register(Curso)