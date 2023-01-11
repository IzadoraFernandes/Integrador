from django.shortcuts import render,  redirect
from .forms import CustomUserCreateForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib import messages
    
class CreateUserView(CreateView):
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

def minhas_reservas(request):
    return render(request, 'minhas_reservas.html')

def usuarios(request):
    return render(request, 'usuarios.html')

#from django.views.generic import TemplateView

#class Cadastrar_labView(TemplateView):
    #template_name = 'cadastrar_lab.html'