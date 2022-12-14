from django.shortcuts import render

def cadastrar_usuario(request):
    return render(request, 'cadastrar_usuario.html')

def login(request):
    return render(request, 'login.html')

def minhas_reservas(request):
    return render(request, 'minhas_reservas.html')

def usuarios(request):
    return render(request, 'usuarios.html')