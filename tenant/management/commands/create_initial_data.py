from django.core.management.base import BaseCommand
from tenant.models import Tenant
from users.models import User
from django.db import transaction

class Command(BaseCommand):
    help = 'Crea los tenants y usuarios iniciales para el sistema'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creando datos iniciales...'))
        
        with transaction.atomic():
            # Crear super admin
            try:
                super_admin = User.objects.create_superuser(
                    username='alex',
                    email='alex@admin.com',
                    password='alex123',
                    role='super_admin'
                )
                self.stdout.write(self.style.SUCCESS(f'Super Admin creado: {super_admin.username}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al crear Super Admin: {str(e)}'))
            
            # Crear Tenant 1 - Clínica 1
            try:
                tenant1 = Tenant.objects.create(
                    name='Clínica 1',
                    slug='clinica1',
                    is_active=True
                )
                self.stdout.write(self.style.SUCCESS(f'Tenant creado: {tenant1.name}'))
                
                # Crear tenant admin para Clínica 1
                tenant_admin1 = User.objects.create_user(
                    username='alex1',
                    email='alex1@clinica1.com',
                    password='clinica1',
                    role='tenant_admin',
                    tenant=tenant1,
                    is_staff=True
                )
                self.stdout.write(self.style.SUCCESS(f'Tenant Admin creado: {tenant_admin1.username} para {tenant1.name}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al crear Tenant 1: {str(e)}'))
            
            # Crear Tenant 2 - Clínica 2
            try:
                tenant2 = Tenant.objects.create(
                    name='Clínica 2',
                    slug='clinica2',
                    is_active=True
                )
                self.stdout.write(self.style.SUCCESS(f'Tenant creado: {tenant2.name}'))
                
                # Crear tenant admin para Clínica 2
                tenant_admin2 = User.objects.create_user(
                    username='alex2',
                    email='alex2@clinica2.com',
                    password='clinica2',
                    role='tenant_admin',
                    tenant=tenant2,
                    is_staff=True
                )
                self.stdout.write(self.style.SUCCESS(f'Tenant Admin creado: {tenant_admin2.username} para {tenant2.name}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al crear Tenant 2: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS('Datos iniciales creados correctamente'))