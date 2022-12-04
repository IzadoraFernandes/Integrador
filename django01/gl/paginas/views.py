from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class LoginView(TemplateView):
    template_name = "login.html"

class Cadastrar_labsView(TemplateView):
    template_name = "cadastrar_lab.html"

class Cadastrar_salaView(TemplateView):
    template_name = "cadastrar_sala.html"

class Cadastrar_usuarioView(TemplateView):
    template_name = "cadastrar_usuario.html"

class InformaticaView(TemplateView):
    template_name = "informatica"




