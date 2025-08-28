from django.contrib import admin
from .models import Paciente

# Register your models here.

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'dni', 'clinica', 'ubigeo', 'activo', 'fecha_registro']
    list_filter = ['clinica', 'activo', 'ubigeo__departamento']
    search_fields = ['nombres', 'apellidos', 'dni']
    list_per_page = 20
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('clinica', 'nombres', 'apellidos', 'dni', 'fecha_nacimiento')
        }),
        ('Contacto', {
            'fields': ('telefono', 'email', 'direccion', 'ubigeo')
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
    )
