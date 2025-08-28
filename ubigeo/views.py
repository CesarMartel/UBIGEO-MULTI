from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Ubigeo
from clinica.models import Clinica

# Create your views here.

def listar_ubigeos(request, clinica_id):
    """Lista ubigeos filtrados por clínica"""
    clinica = get_object_or_404(Clinica, id=clinica_id)
    ubigeos = Ubigeo.get_for_clinica(clinica_id)
    
    context = {
        'clinica': clinica,
        'ubigeos': ubigeos
    }
    return render(request, 'ubigeo/listar.html', context)

def crear_ubigeo(request, clinica_id):
    """Crear nuevo ubigeo para una clínica específica"""
    clinica = get_object_or_404(Clinica, id=clinica_id)
    
    if request.method == 'POST':
        departamento = request.POST.get('departamento')
        provincia = request.POST.get('provincia')
        distrito = request.POST.get('distrito')
        codigo_postal = request.POST.get('codigo_postal')
        
        # Verificar si ya existe
        if Ubigeo.objects.filter(
            clinica=clinica,
            departamento=departamento,
            provincia=provincia,
            distrito=distrito
        ).exists():
            messages.error(request, 'Este ubigeo ya existe para esta clínica.')
        else:
            Ubigeo.objects.create(
                clinica=clinica,
                departamento=departamento,
                provincia=provincia,
                distrito=distrito,
                codigo_postal=codigo_postal
            )
            messages.success(request, 'Ubigeo creado exitosamente.')
            return redirect('ubigeo:listar', clinica_id=clinica_id)
    
    context = {'clinica': clinica}
    return render(request, 'ubigeo/crear.html', context)

def ubigeos_por_clinica_json(request, clinica_id):
    """API endpoint para obtener ubigeos de una clínica en formato JSON"""
    ubigeos = Ubigeo.get_for_clinica(clinica_id)
    data = [
        {
            'id': ubigeo.id,
            'departamento': ubigeo.departamento,
            'provincia': ubigeo.provincia,
            'distrito': ubigeo.distrito,
            'texto_completo': str(ubigeo)
        }
        for ubigeo in ubigeos
    ]
    return JsonResponse({'ubigeos': data})
