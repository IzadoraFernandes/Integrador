from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView
from .forms import  CadastrarReservaModelForm, CadastrarSalaModelForm
from django.urls import reverse_lazy
from .models import Reserva, Sala

#from braces.views import GroupRequiredMixin


class Cadastrar_reservaView(CreateView): #GroupRequiredMixin
    model = Reserva
    #group_required = u"Professores"
    form_class = CadastrarReservaModelForm
    success_url = reverse_lazy('minhas_reservas')
    template_name= 'cadastrar_reserva.html'
    
    
class Cadastrar_salaView(CreateView):
    model = Sala
    #group_required = u"Coapac"
    form_class = CadastrarSalaModelForm
    success_url = reverse_lazy('menu_salas')
    template_name= 'cadastrar_sala.html'
    
class InformaticaView(TemplateView):
    
    template_name= 'informatica.html'
    
class ApiculturaView(TemplateView):
    
    template_name= 'apicultura.html'
    
class AlimentosView(TemplateView):
    
    template_name= 'alimentos.html'
    
class QuimicaView(TemplateView):
    
    template_name= 'quimica.html'





