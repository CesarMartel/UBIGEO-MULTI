from django.db import models
from django.db.models.query import QuerySet
from django.apps import apps
from threading import local

# Almacenamiento local para el tenant activo
_thread_locals = local()

def get_current_tenant():
    """
    Obtiene el tenant activo del contexto actual
    """
    return getattr(_thread_locals, 'tenant', None)

def set_current_tenant(tenant):
    """
    Establece el tenant activo en el contexto actual
    """
    setattr(_thread_locals, 'tenant', tenant)

class TenantQuerySet(QuerySet):
    """
    QuerySet que filtra automáticamente por el tenant activo
    """
    def _filter_by_tenant(self, queryset):
        tenant = get_current_tenant()
        
        # Si hay un tenant activo y el modelo tiene un campo tenant, filtrar
        if tenant and hasattr(self.model, 'tenant'):
            return queryset.filter(tenant=tenant)
        return queryset
    
    def all(self):
        return self._filter_by_tenant(super().all())
    
    def filter(self, *args, **kwargs):
        return self._filter_by_tenant(super().filter(*args, **kwargs))
    
    def get(self, *args, **kwargs):
        return self._filter_by_tenant(super()).get(*args, **kwargs)

class TenantManager(models.Manager):
    """
    Manager que utiliza TenantQuerySet para filtrar automáticamente por tenant
    """
    def get_queryset(self):
        return TenantQuerySet(self.model, using=self._db)