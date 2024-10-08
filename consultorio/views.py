from django.shortcuts import render

def inicio(request):
    return render(request, 'consultorio/inicio.html')  # Renderiza o template 'inicio.html'


def consultorio(request):
    return render(request, 'consultorio/consultorio.html')  # Renderiza o template 'inicio.html'


def login(request):
    return render(request, 'consultorio/login.html')  # Renderiza o template 'inicio.html'

def sobrenos(request):
    return render(request, 'consultorio/sobrenos.html')  # Renderiza o template 'inicio.html'

def tecnologias(request):
    return render(request, 'consultorio/tecnologias.html')  # Renderiza o template 'inicio.html'

def tratamentos(request):
    return render(request, 'consultorio/tratamentos.html')  # Renderiza o template 'inicio.html'

def cadastro(request):
    return render(request, 'consultorio/cadastro.html')  # Renderiza o template 'inicio.html'




