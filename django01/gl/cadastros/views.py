from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Sala, Reserva


class SalaCreate(CreateView):
    model = Sala
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ReservaCreate(CreateView):
    model = Reserva
    fields = ['nome', 'date', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')



