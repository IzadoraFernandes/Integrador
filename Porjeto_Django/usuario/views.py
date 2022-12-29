from django.shortcuts import render
from .forms import RegisterForm

def cadastrar_usuario(request):
    if request.POST:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    return render(request, 'cadastrar_usuario.html', {
        'form' : form,
    })


def login(request):
    return render(request, 'login.html')

def minhas_reservas(request):
    return render(request, 'minhas_reservas.html')

def usuarios(request):
    return render(request, 'usuarios.html')

#from django.views.generic import TemplateView

#class Cadastrar_labView(TemplateView):
    #template_name = 'cadastrar_lab.html'