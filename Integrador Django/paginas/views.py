from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse 
'''from .models import '''

class IndexView(TemplateView):
    template_name = "index.html"

class LoginView(TemplateView):
    template_name = "login.html"

class CriarusuarioView(TemplateView):
    template_name = "from_cadastro_usuario.html"

class InformaticaView(TemplateView):
    template_name = "from_reserva_lab_informatica.html"

class ApiculturaView(TemplateView):
    template_name = "from_reserva_lab_apicultura.html"

class AlimentosView(TemplateView):
    template_name = "from_reserva_lab_alimentos.html"

class QuimicaView(TemplateView):
    template_name = "from_reserva_lab_quimica.html"

class MinhasreservasView(TemplateView):
    template_name = "minhas_reservas.html"

class CriarnovolabView(TemplateView):
    template_name = "from_cadastrar_novo_lab.html"

class CriarnovasalaView(TemplateView):
    template_name = "from_cadastrar_nova_sala.html"

class SobreView(TemplateView):
    template_name = "sobre.html"

'''def processa_formulario(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')

    return HttpResponse(f"{nome} {email}")'''

'''def index(request):
    context = { }
    return render(request, 'index.html', context)'''