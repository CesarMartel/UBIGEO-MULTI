from django.db import models

# Create your models here.

class Clinica(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Clínica"
        verbose_name_plural = "Clínicas"
    
    def __str__(self):
        return self.nombre
