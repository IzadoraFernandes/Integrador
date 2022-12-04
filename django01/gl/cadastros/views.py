from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Campo, Atividade

class CampoCreate(CreateView):
    model = Campo
    fields = ['nome',  'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['nome', 'capacidade', 'numero', 'bloco','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')