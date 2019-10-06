from django.shortcuts import render
from curso.models import Curso, Apostila, Aula

cursos = Curso.objects.all()
aulas = Aula.objects.all()
apostilas = Apostila.objects.all()
args = {'cursos': cursos, 'aulas': aulas, 'apostilas': apostilas}

def index(request):
    return render(request, 'index.html', args)

def cadastro(request):
    return render(request, 'cadastro.html', {})

def login(request):
    return render(request, 'login.html', {})

def area(request):
    return render(request, 'area.html', args)

def areaInfo(request):
    return render(request, 'area-info.html', {})
