from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.views.generic import TemplateView
from .forms import CadastrarReservaModelForm, CadastrarSalaModelForm
from django.urls import reverse_lazy
from .models import Reserva, Sala
from usuario.models import CustomUser
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from utilits.test import test
from datetime import date

#from braces.views import GroupRequiredMixin


class CadastrarReservaView(CreateView):  # GroupRequiredMixin
    model = Reserva
    #group_required = u"Professores"
    form_class = CadastrarReservaModelForm
    success_url = reverse_lazy('minhas_reservas')
    template_name = 'cadastrar_reserva.html'

    def get(self, request):
        salas = Sala.objects.all()
        return render(request, 'cadastrar_reserva.html', {'form': self.get_form(), 'salinhas': salas})

    """def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        #self.object.atributo = “algo”
        # Salva o objeto novamente
        self.object.save()
        return url"""

    """def __init__(self, user=None, *args, **kwargs):
        super(CustomUser, self).__init__(*args, **kwargs)
        # my_field = MyModel.objects.filter(user=user)
        if user.is_authenticated:
            print(user)
        else:
            print('Não')"""

    



class ReservaListView(ListView):  # GroupRequiredMixin
    model = Reserva
    #group_required = u"Professores"
    template_name = 'minhas_reservas.html'
    allow_empty = True


class ReservaUpdateView(UpdateView):
    model = Reserva
    form_class = CadastrarReservaModelForm
    template_name = 'cadastrar_reserva.html'
    success_url = reverse_lazy('minhas_reservas')

    # Altera a query para buscar o objeto do usuário logado
    '''def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Reserva, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object'''

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        salas = Sala.objects.all()
        kwargs["salinhas"] = salas
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        return super().get_context_data(**kwargs)


class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'delete_reserva.html'
    success_url = reverse_lazy('minhas_reservas')


class CadastrarSalaView(CreateView):
    model = Sala
    #group_required = u"Coapac"
    form_class = CadastrarSalaModelForm
    success_url = reverse_lazy('salas')
    template_name = 'cadastrar_sala.html'


class SalasListView(ListView):
    model = Sala
    queryset = Sala.objects.all()
    template_name = 'salas.html'
    allow_empty = True


class SalasUpdateView(UpdateView):
    model = Sala
    form_class = CadastrarSalaModelForm
    template_name = 'cadastrar_sala.html'
    success_url = reverse_lazy('salas')


class SalasDeleteView(DeleteView):
    model = Sala
    template_name = 'delete_sala.html'
    success_url = reverse_lazy('salas')
