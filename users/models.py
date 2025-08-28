from django.db import models
from django.contrib.auth.models import AbstractUser
from tenant.models import Tenant

class User(AbstractUser):
    """
    Modelo de usuario extendido con roles y relación con tenant
    """
    ROLE_CHOICES = (
        ('super_admin', 'Super Admin'),
        ('tenant_admin', 'Tenant Admin'),
        ('user', 'Usuario'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    tenant = models.ForeignKey(
        Tenant, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='users'
    )
    
    def is_super_admin(self):
        return self.role == 'super_admin'
    
    def is_tenant_admin(self):
        return self.role == 'tenant_admin'
    
    def save(self, *args, **kwargs):
        # Asegurarse de que super_admin no tenga tenant asignado
        if self.role == 'super_admin':
            self.tenant = None
            self.is_staff = True
            self.is_superuser = True
        # Asegurarse de que tenant_admin y user tengan tenant asignado
        elif self.role in ['tenant_admin', 'user'] and not self.tenant:
            raise ValueError("Los usuarios de tipo tenant_admin y user deben tener un tenant asignado")
        
        # Dar permisos de administración a los tenant_admin
        if self.role == 'tenant_admin':
            self.is_staff = True
            self.is_superuser = False
        
        super().save(*args, **kwargs)
