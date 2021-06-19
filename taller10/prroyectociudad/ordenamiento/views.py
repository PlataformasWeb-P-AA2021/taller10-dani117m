
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import *

# importar los formularios de forms.py 
from ordenamiento.forms import *

# Create your views here.
def index(request):
    """
        Listar los registros del modelo Estudiante, 
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    parroquias = Parroquia.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'parroquias': parroquias, 'parroquiasV': len(parroquias)}
    return render(request, 'index.html', informacion_template)

def obtener_barrios(request, id):
    """
        Listar los registros del modelo Estudiante, 
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    barrios = Barrio.objects.get(pk=id)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'barrios': barrios}
    return render(request, 'listabarrios.html', informacion_template)


def crear_parroquia(request):
    """
    """
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearEstudiante.html', diccionario) 


def editar_parroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario) 

def crear_barrio(request):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia}

    return render(request, 'crearBarrio.html', diccionario) 


def editar_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario) 




