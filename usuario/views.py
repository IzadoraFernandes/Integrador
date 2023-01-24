from django.shortcuts import render,  redirect
from .forms import CustomUserCreateForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib import messages
from django.views.generic import ListView
from cadastros.models import Reserva
from django.core.paginator import Paginator
#from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

class CreateUserView(LoginRequiredMixin, CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'cadastrar_usuario.html'
    model = CustomUser

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response
    
    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        print("###")
        return self.render_to_response(self.get_context_data(form=form))

def login(request):
    return render(request, 'login.html')


"""class MinhasReservasView(LoginRequiredMixin , ListView):
    model = Reserva
    #group_required = u"Professores"
    #context_object_name = 'minhas_reservas'
    queryset = Reserva.objects.all()
    paginate_by = 10
    template_name = 'minhas_reservas.html

    def get_queryset(self):
        return super().get_queryset()'"""

def listaDeReserva(request):
    template_name = 'minhas_reservas.html'
    object_list = Reserva.objects.filter(usuario=request.user)
    print ("algummmmmmmmmm")
    context = {
        "object_list":  object_list,
    }   

    return render(request, template_name, context)


def usuarios(request):
    return render(request, 'usuarios.html')

