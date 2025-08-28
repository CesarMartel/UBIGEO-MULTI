from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .managers import get_current_tenant

class TenantFilter(SimpleListFilter):
    """
    Filtro para mostrar solo los objetos del tenant actual o todos si es super_admin
    """
    title = 'Tenant'
    parameter_name = 'tenant'

    def lookups(self, request, model_admin):
        # Solo mostrar la opción "Todos" para super_admin
        if request.user.is_superuser:
            return [('all', 'Todos')]
        return []

    def queryset(self, request, queryset):
        # Si no es super_admin, filtrar por el tenant del usuario
        if not request.user.is_superuser and hasattr(request.user, 'tenant') and request.user.tenant:
            return queryset.filter(tenant=request.user.tenant)
        return queryset