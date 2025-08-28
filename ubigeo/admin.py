from django.contrib import admin
from .models import Ubigeo

# Register your models here.

@admin.register(Ubigeo)
class UbigeoAdmin(admin.ModelAdmin):
    list_display = ['departamento', 'provincia', 'distrito', 'clinica', 'activo', 'fecha_creacion']
    list_filter = ['clinica', 'activo', 'departamento']
    search_fields = ['departamento', 'provincia', 'distrito']
    list_per_page = 20
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Si el usuario tiene permisos limitados, filtrar por clínica
        return qs
    
    fieldsets = (
        ('Información de Ubicación', {
            'fields': ('clinica', 'departamento', 'provincia', 'distrito', 'codigo_postal')
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
    )
