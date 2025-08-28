from django.contrib import admin
from .models import Paciente
from tenant.admin_mixins import TenantAdminMixin

@admin.register(Paciente)
class PacienteAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'telefono', 'email')
    search_fields = ('nombre', 'apellido', 'dni')
    list_filter = ('tenant',)
