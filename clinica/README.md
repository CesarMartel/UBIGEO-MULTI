# Aplicación Clinica

Esta aplicación gestiona la información de las clínicas médicas en el sistema.

## Estructura de archivos

- **models.py**: Define el modelo de datos para las clínicas.
- **admin.py**: Configuración para la administración de clínicas en el panel de administración de Django.
- **views.py**: Contiene las vistas para mostrar y manipular los datos de las clínicas.
- **migrations/**: Contiene los archivos de migración para la base de datos.

## Modelo de datos

El modelo principal `Clinica` contiene los siguientes campos:
- `nombre`: Nombre de la clínica
- `direccion`: Dirección física de la clínica
- `telefono`: Número de contacto
- `email`: Correo electrónico de contacto
- `activo`: Estado de la clínica (activo/inactivo)
- `fecha_creacion`: Fecha y hora de registro en el sistema

## Funcionalidad

Esta aplicación sirve como base para todo el sistema, ya que:
1. Cada clínica puede tener múltiples pacientes
2. Cada clínica puede tener múltiples ubicaciones geográficas (ubigeos)
3. Las citas médicas están asociadas a clínicas específicas

## Consideraciones

- Al crear una nueva clínica, se debe asegurar que los datos de contacto sean correctos.
- Una clínica puede ser desactivada (campo `activo` = False) sin eliminarla del sistema, lo que permite mantener el historial.
- Todas las demás entidades del sistema (pacientes, citas, ubigeos) están relacionadas con una clínica específica.