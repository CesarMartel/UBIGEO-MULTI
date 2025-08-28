from django.contrib import admin
from .models import Clinica

# Register your models here.

@admin.register(Clinica)
class ClinicaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'email', 'activo', 'fecha_creacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['nombre', 'email']
    list_per_page = 20
    
    fieldsets = (
        ('Información General', {
            'fields': ('nombre', 'direccion')
        }),
        ('Contacto', {
            'fields': ('telefono', 'email')
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
    )
