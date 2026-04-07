from django.contrib import admin
from .models import Estudiante

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'apellido', 'email', 'programa', 'semestre', 'activo')
    list_filter = ('activo', 'programa', 'semestre')
    search_fields = ('codigo', 'nombre', 'apellido', 'email')
    list_per_page = 20
    ordering = ('codigo',)
