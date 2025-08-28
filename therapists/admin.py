from django.contrib import admin
from .models import Terapeuta
from tenant.admin_mixins import TenantAdminMixin

@admin.register(Terapeuta)
class TerapeutaAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'especialidad', 'dni', 'telefono', 'email')
    search_fields = ('nombre', 'apellido', 'dni')
    list_filter = ('especialidad', 'tenant')