from django.shortcuts import render
from django.http import Http404
from curso.models import Curso, Apostila, Aula
from django.template.defaulttags import register

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

def pagina404(request, param):  
  if not param:  
    raise Http404  
  return render_to_response(request, '404.html', {})  

def areaInfo(request):
    return render(request, 'area-info.html', {})

@register.simple_tag
def areaCurso(request, id):
    id = Curso.objects.get(id=id)
    aulas = Aula.objects.filter(curso__titulo=id.titulo).values().all()
    apostilas = Apostila.objects.all()

    context = {
        "curso": id,
        "aulas": aulas,
        "apostilas": apostilas,
    }

    return render(request, 'area-curso.html', context)

@register.simple_tag
def pegarApostilas(aulaID):
    return Apostila.objects.filter(aulas__id=aulaID).values().all().order_by('numero')
