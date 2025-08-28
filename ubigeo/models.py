from django.db import models
from clinica.models import Clinica

# Create your models here.

class Ubigeo(models.Model):
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, related_name='ubigeos')
    departamento = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Ubigeo"
        verbose_name_plural = "Ubigeos"
        unique_together = ['clinica', 'departamento', 'provincia', 'distrito']
    
    def __str__(self):
        return f"{self.departamento} - {self.provincia} - {self.distrito}"
    
    @classmethod
    def get_for_clinica(cls, clinica_id):
        """Método para obtener ubigeos filtrados por clínica"""
        return cls.objects.filter(clinica_id=clinica_id, activo=True)
