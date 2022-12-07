from django.shortcuts import render

def cadastrar_lab(request):
    return render(request, 'cadastrar_lab.html')

def cadastrar_reserva(request):
    return render(request, 'cadastrar_reserva.html')

def cadastrar_sala(request):
    return render(request, 'cadastrar_sala.html')

def informatica(request):
    return render(request, 'informatica.html')

def alimentos(request):
    return render(request, 'alimentos.html')

def apicultura(request):
    return render(request, 'apicultura.html')

def quimica(request):
    return render(request, 'quimica.html')





