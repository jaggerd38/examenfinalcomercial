from django.shortcuts import render, render, get_object_or_404, redirect
from django.contrib import messages
from .forms import GradoForm
from notas.models import Grado, Materia, Pensum
from django.contrib.auth.decorators import login_required

def grado_nuevo(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(grado=formulario.cleaned_data['grado'],
                    seccion = formulario.cleaned_data['seccion'],
                    descripcion = formulario.cleaned_data['descripcion'])
            for materia_id in request.POST.getlist('materias'):
                pensum = Pensum(materia_id=materia_id, grado_id = grado.id)
                pensum.save()
            return redirect('ver_grado', pk=grado.pk)
    else:
        formulario = GradoForm()
    return render(request, 'notas/grado_editar.html', {'formulario': formulario})

def detalle_grado(request, pk):
    grado = get_object_or_404(Grado, pk=pk)
    return render(request, 'notas/detalle_grado.html', {'p': grado})
