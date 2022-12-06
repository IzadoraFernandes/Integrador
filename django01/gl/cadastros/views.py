from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Sala, Reserva


class SalaCreate(CreateView):
    sala = Sala.objects.all()
    model = Sala
    fields = ['nome', 'descricao']
    template_name = 'from.html, {"sala": sala}'
    success_url = reverse_lazy('index')

class ReservaCreate(CreateView):
    model = Reserva
    fields = ['nome', 'capacidade', 'numero', 'bloco', 'descricao']
    template_name = 'from.html'
    success_url = reverse_lazy('index')

###################### UPDATE ######################

class SalaUpdate(UpdateView):
    model = Sala
    fields = ['nome', 'descrição']
    template_name = 'form.html'
    success_url = reverse_lazy('index')

class ReservaUpdate(UpdateView):
    model = Reserva
    fields = ['nome', 'capacidade', 'numero', 'bloco', 'descricao']
    template_name = 'from.html'
    success_url = reverse_lazy('index')

