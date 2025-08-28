from django.contrib import admin
from .models import Cita

# Register your models here.

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'fecha_hora', 'clinica', 'estado', 'ubicacion_cita', 'fecha_creacion']
    list_filter = ['clinica', 'estado', 'fecha_hora']
    search_fields = ['paciente__nombres', 'paciente__apellidos', 'motivo']
    list_per_page = 20
    date_hierarchy = 'fecha_hora'
    
    fieldsets = (
        ('Información de la Cita', {
            'fields': ('clinica', 'paciente', 'fecha_hora', 'motivo')
        }),
        ('Ubicación y Estado', {
            'fields': ('ubicacion_cita', 'estado', 'observaciones')
        }),
    )
