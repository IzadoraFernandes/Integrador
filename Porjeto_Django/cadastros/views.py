
from django.views.generic import TemplateView

class Cadastrar_labView(TemplateView):
    template_name = 'cadastrar_lab.html'

class Cadastrar_reservaView(TemplateView):
    template_name= 'cadastrar_reserva.html'
    
class Cadastrar_salaView(TemplateView):
    template_name= 'cadastrar_sala.html'
    
class InformaticaView(TemplateView):
    template_name= 'informatica.html'
    
class ApiculturaView(TemplateView):
    template_name= 'apicultura.html'
    
class AlimentosView(TemplateView):
    template_name= 'alimentos.html'
    
class QuimicaView(TemplateView):
    template_name= 'quimica.html'
    
"""
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
    return render(request, 'quimica.html')"""




