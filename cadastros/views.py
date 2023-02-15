from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.views.generic import TemplateView
from .forms import CadastrarReservaModelForm, CadastrarSalaModelForm
from django.urls import reverse_lazy
from .models import Reserva, Sala
from usuario.models import CustomUser
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from utilits.test import test
from datetime import date
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin

class CadastrarReservaView(LoginRequiredMixin, CreateView):
    model = Reserva
    form_class = CadastrarReservaModelForm
    success_url = reverse_lazy('minhas_reservas')
    template_name = 'cadastrar_reserva.html'

    def get(self, request):
        salas = Sala.objects.all()
        return render(request, 'cadastrar_reserva.html', {'form': self.get_form(), 'salinhas': salas})
        
class ReservaListView(LoginRequiredMixin, ListView):  
    model = Reserva
    template_name = 'minhas_reservas.html'
    allow_empty = True
    paginate_by = 1

class ReservaUpdateView(LoginRequiredMixin, UpdateView):
    model = Reserva
    form_class = CadastrarReservaModelForm
    template_name = 'cadastrar_reserva.html'
    success_url = reverse_lazy('minhas_reservas')

    # Altera a query para buscar o objeto do usuário logado
    """def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Reserva, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object"""

    def get_context_data(self, **kwargs):
        salas = Sala.objects.all()
        kwargs["salinhas"] = salas
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        return super().get_context_data(**kwargs)


class ReservaDeleteView(LoginRequiredMixin, DeleteView):
    model = Reserva
    template_name = 'delete_reserva.html'
    success_url = reverse_lazy('minhas_reservas')


class CadastrarSalaView(LoginRequiredMixin, CreateView):
    model = Sala
    form_class = CadastrarSalaModelForm
    success_url = reverse_lazy('salas')
    template_name = 'cadastrar_sala.html'


class SalasListView(LoginRequiredMixin, ListView):
    model = Sala
    queryset = Sala.objects.all()
    template_name = 'salas.html'
    allow_empty = True
    paginate_by = 2


class SalasUpdateView(LoginRequiredMixin, UpdateView):
    model = Sala
    form_class = CadastrarSalaModelForm
    template_name = 'cadastrar_sala.html'
    success_url = reverse_lazy('salas')


class SalasDeleteView(LoginRequiredMixin, DeleteView):
    model = Sala
    template_name = 'delete_sala.html'
    success_url = reverse_lazy('salas')
