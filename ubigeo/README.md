# Aplicación Ubigeo

Esta aplicación gestiona las ubicaciones geográficas (departamentos, provincias y distritos) en el sistema.

## Estructura de archivos

- **models.py**: Define el modelo de datos para las ubicaciones geográficas.
- **admin.py**: Configuración para la administración de ubigeos en el panel de administración de Django.
- **views.py**: Contiene las vistas para mostrar y manipular los datos de ubicaciones.
- **migrations/**: Contiene los archivos de migración para la base de datos.

## Modelo de datos

El modelo principal `Ubigeo` contiene los siguientes campos:
- `clinica`: Relación con la clínica a la que pertenece la ubicación
- `departamento`: Nombre del departamento
- `provincia`: Nombre de la provincia
- `distrito`: Nombre del distrito
- `codigo_postal`: Código postal (opcional)
- `activo`: Estado de la ubicación (activo/inactivo)
- `fecha_creacion`: Fecha y hora de registro en el sistema

## Funcionalidad

Esta aplicación permite:
1. Registrar ubicaciones geográficas asociadas a clínicas específicas
2. Proporcionar información de ubicación para pacientes y citas
3. Filtrar ubicaciones por clínica mediante el método `get_for_clinica`
4. Mantener un registro organizado de las zonas geográficas donde opera cada clínica

## Consideraciones

- Cada ubicación está vinculada a una clínica específica.
- El sistema garantiza que no haya duplicados de ubicaciones para una misma clínica mediante la restricción `unique_together`.
- Las ubicaciones pueden ser desactivadas (campo `activo` = False) sin eliminarlas del sistema.
- Esta aplicación es fundamental para la organización territorial de pacientes y citas.