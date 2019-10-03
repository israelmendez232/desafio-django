from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def cadastro(request):
    return render(request, 'cadastro.html', {})

def login(request):
    return render(request, 'login.html', {})

def area(request):
    return render(request, 'area.html', {})

def areaInfo(request):
    return render(request, 'area-info.html', {})
