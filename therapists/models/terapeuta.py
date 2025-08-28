from django.db import models
from tenant.models import Tenant
from ubigeo.models import Ubigeo
from tenant.managers import TenantManager

class Terapeuta(models.Model):
    """
    Modelo para representar terapeutas con aislamiento por tenant (clínica)
    """
    tenant = models.ForeignKey(
        Tenant, 
        on_delete=models.CASCADE,
        related_name='terapeutas'
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    ubigeo = models.ForeignKey(
        Ubigeo, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='terapeutas'
    )
    direccion = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Manager personalizado para filtrar por tenant
    objects = TenantManager()
    
    class Meta:
        unique_together = ('tenant', 'dni')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
    
    def save(self, *args, **kwargs):
        # Validar que el ubigeo pertenezca al mismo tenant
        if self.ubigeo and self.tenant and self.ubigeo.tenant != self.tenant:
            raise ValueError("El ubigeo debe pertenecer al mismo tenant que el terapeuta")
        super().save(*args, **kwargs)