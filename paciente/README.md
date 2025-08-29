# Aplicación Paciente

Esta aplicación gestiona la información de los pacientes en el sistema.

## Estructura de archivos

- **models.py**: Define el modelo de datos para los pacientes.
- **admin.py**: Configuración para la administración de pacientes en el panel de administración de Django.
- **views.py**: Contiene las vistas para mostrar y manipular los datos de los pacientes.
- **forms.py**: Define formularios para la creación y edición de pacientes.
- **migrations/**: Contiene los archivos de migración para la base de datos.

## Modelo de datos

El modelo principal `Paciente` contiene los siguientes campos:
- `clinica`: Relación con la clínica a la que pertenece el paciente
- `nombres`: Nombres del paciente
- `apellidos`: Apellidos del paciente
- `dni`: Documento Nacional de Identidad (único)
- `fecha_nacimiento`: Fecha de nacimiento
- `telefono`: Número de contacto
- `email`: Correo electrónico (opcional)
- `direccion`: Dirección física del paciente
- `ubigeo`: Relación con la ubicación geográfica del paciente
- `activo`: Estado del paciente (activo/inactivo)
- `fecha_registro`: Fecha y hora de registro en el sistema

## Funcionalidad

Esta aplicación permite:
1. Registrar nuevos pacientes asociados a una clínica específica
2. Asignar una ubicación geográfica (ubigeo) al paciente
3. Mantener un registro histórico de los pacientes
4. Validar que el ubigeo asignado pertenezca a la misma clínica del paciente

## Consideraciones

- El DNI es un campo único que identifica a cada paciente.
- El sistema valida automáticamente que el ubigeo asignado pertenezca a la misma clínica que el paciente.
- Un paciente puede ser desactivado (campo `activo` = False) sin eliminarlo del sistema, lo que permite mantener el historial.
- Los pacientes están vinculados a una clínica específica y solo pueden tener citas en esa clínica.