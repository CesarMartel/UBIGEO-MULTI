from django.contrib import admin
from .models import Ubigeo
from tenant.admin_mixins import TenantAdminMixin

@admin.register(Ubigeo)
class UbigeoAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'tipo', 'parent')
    search_fields = ('codigo', 'nombre')
    list_filter = ('tipo', 'tenant')
