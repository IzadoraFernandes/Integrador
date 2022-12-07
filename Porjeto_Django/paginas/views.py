from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def menu_sala(request):
    return render(request, 'menu_sala.html')