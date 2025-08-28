from django.contrib import admin
from .models import Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'created_at')
    search_fields = ('name', 'slug')
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}
    
    def get_queryset(self, request):
        """
        Filtrar los tenants según el rol del usuario:
        - super_admin: ve todos los tenants
        - tenant_admin: solo ve su propio tenant
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(id=request.user.tenant.id)
