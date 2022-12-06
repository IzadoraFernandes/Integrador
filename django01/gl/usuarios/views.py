from django.views.generic import TemplateView
from django.shortcuts import render

class LoginView(TemplateView):
    template_name = "login.html"

def cadastrar_usuario(request):
    return render(request, 'cadastrar_usuario.html')