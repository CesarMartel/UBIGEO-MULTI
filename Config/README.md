# Carpeta Config

Esta carpeta contiene la configuración principal del proyecto Django.

## Archivos principales

- **settings.py**: Contiene toda la configuración del proyecto, incluyendo:
  - Configuración de la base de datos MySQL
  - Aplicaciones instaladas
  - Middleware
  - Configuración de plantillas
  - Validadores de contraseñas
  - Configuración de zona horaria y lenguaje

- **urls.py**: Define las URLs principales del proyecto y las redirecciones a las aplicaciones.

- **wsgi.py**: Configuración para el despliegue con WSGI (Web Server Gateway Interface).

- **asgi.py**: Configuración para el despliegue con ASGI (Asynchronous Server Gateway Interface).

## Función

Esta carpeta es el núcleo de configuración del proyecto Django. Cualquier cambio en la configuración global del proyecto debe realizarse aquí. Es especialmente importante para:

1. Añadir nuevas aplicaciones al proyecto
2. Configurar la conexión a la base de datos
3. Modificar la configuración de seguridad
4. Configurar rutas URL principales

## Consideraciones

- El archivo `settings.py` contiene información sensible como la SECRET_KEY y las credenciales de la base de datos. En un entorno de producción, esta información debería estar protegida mediante variables de entorno.
- Cualquier nueva aplicación que se cree debe ser añadida a la lista INSTALLED_APPS en `settings.py`.