from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView
from .forms import CadastrarLaboratorioModelForm, CadastrarReservaModelForm, CadastrarSalaModelForm
from django.urls import reverse_lazy
from .models import Reserva, Sala, Laboratorio

from braces.views import GroupRequiredMixin

class Cadastrar_labView(CreateView, GroupRequiredMixin):
    model = Laboratorio
    group_required = u"Coapac"
    form_class = CadastrarLaboratorioModelForm
    success_url = reverse_lazy('menu_salas')
    template_name = 'cadastrar_lab.html'

class Cadastrar_reservaView(CreateView, GroupRequiredMixin):
    model = Reserva
    group_required = u"Professores"
    form_class = CadastrarReservaModelForm
    success_url = reverse_lazy('minhas_reservas')
    template_name= 'cadastrar_reserva.html'
    
    
class Cadastrar_salaView(CreateView, GroupRequiredMixin):
    model = Sala
    group_required = u"Coapac"
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

"""class TesteView(TemplateView):
    template_name = 'teste.html'
    def get_context_data(self, **kwargs):
        context = super(TesteView, self).get_context_data(**kwargs)
        context['sala'] = Sala.objects.all()
        return context

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




