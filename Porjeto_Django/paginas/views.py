from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def menu_salas(request):
    return render(request, 'menu_salas.html')

def agenda(request):
    return render(request, 'agenda.html')