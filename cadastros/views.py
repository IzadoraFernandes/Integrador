from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.views.generic import TemplateView
from .forms import CadastrarReservaModelForm, CadastrarSalaModelForm
from django.urls import reverse_lazy
from .models import Reserva, Sala
from usuario.models import CustomUser
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from utilits.test import test
from django.contrib.auth.mixins import LoginRequiredMixin


class CadastrarReservaView(LoginRequiredMixin, CreateView): 
    model = Reserva
    form_class = CadastrarReservaModelForm
    success_url = reverse_lazy('minhas_reservas')
    template_name = 'cadastrar_reserva.html'

    def get(self, request):
        salas = Sala.objects.all()
        return render(request, 'cadastrar_reserva.html', {'form': self.get_form(), 'salinhas': salas})


    def post(self, request, *args, **kwargs):
        
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs


"""class ReservaListView(ListView):  # GroupRequiredMixin
    model = Reserva
    #group_required = u"Professores"
    template_name = 'minhas_reservas.html'
    allow_empty = True"""

def listaDeReserva(request):
    template_name = 'minhas_reservas.html'
    object_list = Reserva.objects.filter(usuario=request.user)
    context = {
        "object_list":  object_list,
    }   
    return render(request, template_name, context)


class ReservaUpdateView(LoginRequiredMixin, UpdateView):
    model = Reserva
    form_class = CadastrarReservaModelForm
    template_name = 'cadastrar_reserva.html'
    success_url = reverse_lazy('minhas_reservas')

    # Altera a query para buscar o objeto do usuário logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Reserva, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        salas = Sala.objects.all()
        kwargs["salinhas"] = salas
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs


class ReservaDeleteView(LoginRequiredMixin, DeleteView):
    model = Reserva
    template_name = 'delete_reserva.html'
    success_url = reverse_lazy('minhas_reservas')


class CadastrarSalaView(LoginRequiredMixin, CreateView):
    model = Sala
    form_class = CadastrarSalaModelForm
    success_url = reverse_lazy('salas')
    template_name = 'cadastrar_sala.html'
    

    def post(self, request , *args, **kwargs ):
        print("qualquer coisa")
        return super().post(request, *args, **kwargs)

    

class SalasListView(LoginRequiredMixin, ListView):
    model = Sala
    queryset = Sala.objects.all()
    template_name = 'salas.html'
    allow_empty = True


class SalasUpdateView(LoginRequiredMixin, UpdateView):
    model = Sala
    form_class = CadastrarSalaModelForm
    template_name = 'cadastrar_sala.html'
    success_url = reverse_lazy('salas')


class SalasDeleteView(LoginRequiredMixin, DeleteView):
    model = Sala
    template_name = 'delete_sala.html'
    success_url = reverse_lazy('salas')
