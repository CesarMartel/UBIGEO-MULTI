from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.http import Http404
from .models import Tenant

class TenantMiddleware(MiddlewareMixin):
    """
    Middleware para establecer el tenant activo en cada solicitud.
    Extrae el tenant del subdominio o del parámetro en la URL.
    """
    
    def process_request(self, request):
        # Inicializar tenant como None
        request.tenant = None
        
        # Obtener el tenant del subdominio (ejemplo: clinica1.dominio.com)
        host = request.get_host().split(':')[0]
        subdomain = host.split('.')[0]
        
        # Si estamos en localhost o en desarrollo, intentar obtener el tenant de la URL
        if subdomain == 'localhost' or subdomain == '127':
            tenant_slug = request.GET.get('tenant')
            if tenant_slug:
                try:
                    request.tenant = Tenant.objects.get(slug=tenant_slug, is_active=True)
                except Tenant.DoesNotExist:
                    pass
        else:
            # En producción, obtener el tenant del subdominio
            try:
                request.tenant = Tenant.objects.get(slug=subdomain, is_active=True)
            except Tenant.DoesNotExist:
                # Si no es una ruta pública, devolver 404
                if not self._is_public_path(request.path):
                    raise Http404("Tenant no encontrado")
    
    def _is_public_path(self, path):
        """
        Determina si una ruta es pública (accesible sin tenant)
        """
        public_paths = [
            '/admin/',
            '/api/auth/',
            '/static/',
            '/media/',
        ]
        return any(path.startswith(prefix) for prefix in public_paths)