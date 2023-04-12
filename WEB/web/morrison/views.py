from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from .models import Mapa
from .forms import MapaForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def mapas(request):
    mapas = Mapa.objects.all()
    return render(request, 'mapas/index.html', {'mapas': mapas})

def subir_pedido(request):
    formulario = MapaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('mapas')
    return render(request, 'mapas/subir.html', {'formulario': formulario})
    

def editar(request, id):
    edicion = Mapa.objects.get(id=id)
    formulario = MapaForm(request.POST or None, instance=edicion)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('mapas')
    return render(request, 'mapas/editar.html', {'formulario': formulario})

def eliminar(request, id):
    mapeo = Mapa.objects.get(id=id)
    mapeo.delete()
    return redirect('mapas')