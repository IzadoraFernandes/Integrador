from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from cadastros.models import Reserva, Sala
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'index.html')

def agenda(request):
    return render(request, 'agenda.html')

class ReservaSalaListView(ListView):
    model = Reserva
    queryset = Reserva.objects.all()
    template_name = 'lista_reservas.html'

    """ def get_context_data(self, **kwargs):
        context = super(ReservaSalaListView, self).get_context_data(**kwargs)
        sala = Sala.objects.get(pk=kwargs['pk'])
        reservas = Reserva.objects.all().filter(sala=sala)
        context.update({
            "reservas": reservas,
            "sala": sala
        })

        return context """

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        
        sala = Sala.objects.get(pk=kwargs['pk'])
        reservas = Reserva.objects.all().filter(sala=sala)
        
        context = {
            "reservas": reservas,
            "sala": sala,
        }

        return self.render_to_response(context)
