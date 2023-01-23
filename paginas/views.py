from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from cadastros.models import Reserva, Sala
from django.views.generic import DeleteView


def index(request):
    return render(request, 'index.html')

def agenda(request):
    return render(request, 'agenda.html')

class ReservaSalaListView(ListView):
    model = Reserva
    queryset = Reserva.objects.all()
    template_name = 'agenda.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        
        sala = Sala.objects.get(pk=kwargs['pk'])
        reservas = Reserva.objects.all().filter(sala=sala)
        
        context = {
            "reservas": reservas,
            "sala": sala
        }

        return self.render_to_response(context)
