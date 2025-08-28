from django.contrib import admin

class TenantAdminMixin:
    """
    Mixin para filtrar objetos por tenant en el admin
    """
    
    def get_queryset(self, request):
        """
        Filtrar objetos por tenant según el rol del usuario:
        - super_admin: ve todos los objetos
        - tenant_admin: solo ve objetos de su tenant
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'tenant') and request.user.tenant:
            return qs.filter(tenant=request.user.tenant)
        return qs.none()
    
    def save_model(self, request, obj, form, change):
        """
        Asignar automáticamente el tenant del usuario al objeto
        """
        if not request.user.is_superuser and not obj.tenant_id:
            obj.tenant = request.user.tenant
        super().save_model(request, obj, form, change)
    
    def has_change_permission(self, request, obj=None):
        if not obj:
            return True
        if request.user.is_superuser:
            return True
        return obj.tenant == request.user.tenant
    
    def has_delete_permission(self, request, obj=None):
        if not obj:
            return True
        if request.user.is_superuser:
            return True
        return obj.tenant == request.user.tenant