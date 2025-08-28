from django.db import models
from tenant.models import Tenant
from tenant.managers import TenantManager

class Ubigeo(models.Model):
    """
    Modelo para representar ubicaciones geográficas (departamentos, provincias, distritos)
    con aislamiento por tenant (clínica)
    """
    tenant = models.ForeignKey(
        Tenant, 
        on_delete=models.CASCADE,
        related_name='ubigeos'
    )
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=20,
        choices=[
            ('departamento', 'Departamento'),
            ('provincia', 'Provincia'),
            ('distrito', 'Distrito')
        ]
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    
    # Manager personalizado para filtrar por tenant
    objects = TenantManager()
    
    class Meta:
        unique_together = ('tenant', 'codigo')
        
    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"
