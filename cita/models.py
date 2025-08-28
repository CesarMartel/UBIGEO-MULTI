from django.db import models
from clinica.models import Clinica
from paciente.models import Paciente
from ubigeo.models import Ubigeo

# Create your models here.

class Cita(models.Model):
    ESTADOS = [
        ('programada', 'Programada'),
        ('confirmada', 'Confirmada'),
        ('atendida', 'Atendida'),
        ('cancelada', 'Cancelada'),
    ]
    
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, related_name='citas')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    fecha_hora = models.DateTimeField()
    motivo = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='programada')
    ubicacion_cita = models.ForeignKey(Ubigeo, on_delete=models.SET_NULL, null=True, blank=True, 
                                      help_text="Ubicación donde se realizará la cita")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
    
    def __str__(self):
        return f"Cita {self.paciente} - {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}"
    
    def save(self, *args, **kwargs):
        # Validar que el paciente pertenezca a la misma clínica
        if self.paciente.clinica != self.clinica:
            raise ValueError("El paciente debe pertenecer a la misma clínica de la cita")
        
        # Validar que la ubicación pertenezca a la misma clínica
        if self.ubicacion_cita and self.ubicacion_cita.clinica != self.clinica:
            raise ValueError("La ubicación debe pertenecer a la misma clínica de la cita")
        
        super().save(*args, **kwargs)
