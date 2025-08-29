# Aplicación Cita

Esta aplicación gestiona las citas médicas en el sistema.

## Estructura de archivos

- **models.py**: Define el modelo de datos para las citas médicas.
- **admin.py**: Configuración para la administración de citas en el panel de administración de Django.
- **views.py**: Contiene las vistas para mostrar y manipular los datos de las citas.
- **migrations/**: Contiene los archivos de migración para la base de datos.

## Modelo de datos

El modelo principal `Cita` contiene los siguientes campos:
- `clinica`: Relación con la clínica donde se realiza la cita
- `paciente`: Relación con el paciente que tiene la cita
- `fecha_hora`: Fecha y hora programada para la cita
- `motivo`: Razón de la cita
- `observaciones`: Notas adicionales (opcional)
- `estado`: Estado de la cita (programada, confirmada, atendida, cancelada)
- `ubicacion_cita`: Relación con la ubicación geográfica donde se realizará la cita
- `fecha_creacion`: Fecha y hora de registro en el sistema

## Funcionalidad

Esta aplicación permite:
1. Programar citas para pacientes en clínicas específicas
2. Gestionar el ciclo de vida de las citas (programación, confirmación, atención, cancelación)
3. Asignar ubicaciones específicas para las citas
4. Mantener un registro histórico de todas las citas

## Consideraciones

- Las citas están vinculadas tanto a una clínica como a un paciente específico.
- El sistema permite asignar diferentes estados a las citas para seguir su progreso.
- La ubicación de la cita puede ser diferente a la ubicación del paciente, permitiendo flexibilidad en la atención.
- Es importante mantener actualizado el estado de las citas para tener un registro preciso de la atención.