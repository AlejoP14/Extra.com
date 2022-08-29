from django.shortcuts import get_object_or_404, render
from InicioCabaña.forms import FormArchivos
from .models import Archivos, RegistroCabaña
from django.contrib import messages 

def inicio(request):
    registros = RegistroCabaña.objects.filter(oferta="Si")
    return render(request, 'inicio/principal.html', {'registros': registros})

def catalogo(request):
    registros = RegistroCabaña.objects.all()
    return render(request, 'inicio/catalogo.html', {'registros': registros})

def comentarios(request):
    return render(request, 'inicio/comentario.html')

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            nombre =request.POST['nombre']
            email =request.POST['email']
            comentario =request.POST['comentario']
            archivo =request.FILES['archivo']
            insert = Archivos(nombre=nombre, email=email ,comentario=comentario ,archivo=archivo)
            insert.save()
            archivos = Archivos.objects.all()
            return render(request, 'inicio/comentario.html', {'archivos':archivos})
        else:
            messages.error(request, 'Error al subir el archivo')
    else:
        return render(request, 'inicio/comentario.html', {'archivo':Archivos})

def consultasSQL(request):
    archivos=Archivos.objects.raw('SELECT id, nombre, email, comentario, archivo FROM InicioCabaña_archivos')
    return render (request, 'inicio/comentario.html', {'archivos':archivos})

def eliminar(request, id, confirmacion = 'inicio/Eliminacion.html'):
    archivo = get_object_or_404(Archivos, id=id)
    if request.method == 'POST':
        archivo.delete()
        archivos = Archivos.objects.all()
        return render(request, 'inicio/comentario.html', {'archivos': archivos})
    return render(request, confirmacion, {'object': archivo})

def consultarComentario(request, id):
    archivo = Archivos.objects.get(id=id)
    return render(request, 'inicio/EditarComentario.html', {'archivo': archivo})

# Editar
def editarComentario(request, id):
    archivo = get_object_or_404(Archivos, id=id)
    form = FormArchivos(request.POST, instance=archivo)
    if form.is_valid():
        form.save()
        archivos = Archivos.objects.all()
        return render(request, 'inicio/comentario.html', {'archivos': archivos})
    return render(request, 'inicio/comentario.html', {'archivo':archivo })
