from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView
from .forms import CadastrarLaboratorioModelForm, CadastrarReservaModelForm, CadastrarSalaModelForm
from django.urls import reverse_lazy
from .models import Reserva, Sala, Laboratorio


class Cadastrar_labView(CreateView):
    model = Laboratorio
    form_class = CadastrarLaboratorioModelForm
    success_url = reverse_lazy('menu_salas')
    template_name = 'cadastrar_lab.html'

class Cadastrar_reservaView(CreateView):
    model = Reserva
    form_class = CadastrarReservaModelForm
    success_url = reverse_lazy('minhas_reservas')
    template_name= 'cadastrar_reserva.html'
    
class Cadastrar_salaView(CreateView):
    model = Sala
    form_class = CadastrarSalaModelForm
    success_url = reverse_lazy('menu_salas')
    template_name= 'cadastrar_sala.html'
    
class InformaticaView(TemplateView):
    form_class = CadastrarLaboratorioModelForm
    template_name= 'informatica.html'
    
class ApiculturaView(TemplateView):
    form_class = CadastrarLaboratorioModelForm
    template_name= 'apicultura.html'
    
class AlimentosView(TemplateView):
    form_class = CadastrarLaboratorioModelForm
    template_name= 'alimentos.html'
    
class QuimicaView(TemplateView):
    form_class = CadastrarLaboratorioModelForm
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




