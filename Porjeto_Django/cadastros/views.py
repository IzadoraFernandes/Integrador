from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.views.generic import TemplateView
from .forms import  CadastrarReservaModelForm, CadastrarSalaModelForm
from django.urls import reverse_lazy
from .models import Reserva, Sala
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

#from braces.views import GroupRequiredMixin

class CadastrarReservaView(CreateView): #GroupRequiredMixin
    model = Reserva
    #group_required = u"Professores"
    form_class = CadastrarReservaModelForm
    success_url = reverse_lazy('minhas_reservas')
    template_name= 'cadastrar_reserva.html'

    def get(self, request):
        salas = Sala.objects.all()
        return render(request, 'cadastrar_reserva.html', {'form': self.get_form(), 'salinhas': salas})
    
    def form_valid(self, form):
        """salas = Sala.objects.all()
        self.object = form
        print(self.object)
        '''print(self.object.data)
        print(self.object.numero)
        print(self.object.sala.numero)
        print(self.object.sala)
        print(self.object.sala.id)'''
        for salinha in salas:
            if self.object.data == salinha.data and self.object.horario == salinha.horario and self.object.sala.id == salinha.id:
                print('não salva')
                break"""
        self.object = form.save()
        return super().form_valid(form)

class ReservaListView(ListView): #GroupRequiredMixin
    model = Reserva
    #group_required = u"Professores"
    template_name = 'teste.html'
    allow_empty = True

class ReservaUpdateView(UpdateView):
    model = Reserva
    form_class = CadastrarReservaModelForm
    template_name= 'cadastrar_reserva.html'
    success_url= reverse_lazy('minhas_reservas')

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        salas = Sala.objects.all()
        kwargs["salinhas"] = salas
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        return super().get_context_data(**kwargs)

class ReservaDeleteView(DeleteView):
    model = Reserva 
    template_name= 'delete_reserva.html'   
    success_url= reverse_lazy('minhas_reservas')


class CadastrarSalaView(CreateView):
    model = Sala
    #group_required = u"Coapac"
    form_class = CadastrarSalaModelForm
    success_url = reverse_lazy('menu_salas')
    template_name= 'cadastrar_sala.html'


class SalasListView(ListView):
    model = Sala
    queryset = Sala.objects.all()
    template_name= 'salas.html'
    allow_empty = True
    

class SalasUpdateView(UpdateView):
    model = Sala
    form_class = CadastrarSalaModelForm
    template_name= 'cadastrar_sala.html'
    success_url= reverse_lazy('salas')


class SalasDeleteView(DeleteView):
    model = Sala 
    template_name= 'delete_sala.html'   
    success_url= reverse_lazy('salas')

