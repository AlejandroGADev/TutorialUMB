from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import Alumnos
# Create your views here.
from  .forms import AlumnosFORM


def alumnos(request):
    filtro = Alumnos.objects.all()
    return render(request, 'alumnos.html', {'filtro':filtro})



def formularip(request):
    if request.method == 'POST':
        form = AlumnosFORM(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/formulario/')
    else:
        form = AlumnosFORM()
    return render(request, 'formulario.html', {'form':form})