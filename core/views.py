from core.forms import MascotaForm
from django.shortcuts import render, redirect
from .models import Mascota

# Create your views here.

#funcion para mostrar paginas

def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def gato(request):
    mascotas = Mascota.objects.filter(especie=1) #Definimos que la especie 1 (gato) se muestre aquí


    datos = {
        'mascotas': mascotas
    }

    return render(request, 'core/gato.html', datos)

def perro(request):
    mascotas = Mascota.objects.filter(especie=2) #Definimos que la especie 2 (perro) se muestre aquí


    datos = {
        'mascotas': mascotas
    }

    return render(request, 'core/perro.html', datos)

def verMascota(request,id):

    mascota = Mascota.objects.get(chip = id)

    datos = {
        'mascota': mascota
    }

    return render(request, 'core/verMascota.html', datos)

def contacto(request):
    return render(request, 'core/contacto.html')

def donar(request):
    return render(request, 'core/donar.html')

def tablaMascotas(request):

    mascotas = Mascota.objects.all()

    datos = {
        'mascotas': mascotas
    }

    return render(request, 'core/tablaMascotas.html', datos)


def form_mascota(request):

    datos = {
        'form': MascotaForm()
    }

    if request.method == 'POST':
        formulario = MascotaForm(request.POST, files=request.FILES)


        if formulario.is_valid:
            formulario.save()

            datos['mensaje'] = "Datos guardados correctamente"
        else:
            datos['mensaje'] = "Error al ingresar Datos"


    return render(request, 'core/form_mascota.html', datos)


def form_ver_mascota(request,id):

    mascota = Mascota.objects.get(chip = id)

    datos = {
        'mascota': mascota
    }


    return render(request, 'core/form_ver_mascota.html', datos)



def form_mod_mascota(request,id):

    mascota = Mascota.objects.get(chip = id)

    datos = {
        'form': MascotaForm(instance = mascota)
    }

    if request.method == 'POST':
        formulario = MascotaForm(data = request.POST, instance = mascota, files=request.FILES)


        if formulario.is_valid:
            formulario.save()

            datos['mensaje'] = "Datos modificados correctamente"
        else:
            datos['mensaje'] = "Error al ingresar Datos"
        datos['form'] = MascotaForm(instance=Mascota.objects.get(chip = id))

    return render(request, 'core/form_mod_mascota.html', datos)

def form_del_mascota(request,id):

    mascota = Mascota.objects.get(chip = id)

    mascota.delete()

    return redirect(to = 'tablaMascotas')