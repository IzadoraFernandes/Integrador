from django.urls import path
from .views import IndexView, LoginView, Cadastrar_labsView, Cadastrar_salaView,  Cadastrar_usuarioView, InformaticaView #, CampoCreate, AtividadeCreate

urlpatterns = [

    path('', IndexView.as_view(), name= 'index'),
    path('login/', LoginView.as_view(), name= 'login'),
    path('cadastrar_lab', Cadastrar_labsView.as_view(), name= 'cadastrar_lab'),
    path('cadastrar_sala', Cadastrar_salaView.as_view(), name= 'cadastrar_sala'),
    path('cadastrar_usuario', Cadastrar_usuarioView.as_view(), name= 'cadastrar_usuario'),
    path('informatica', InformaticaView.as_view(), name= 'informatica'),
    #path('cadastrar_campo', CampoCreate.as_view(), name= 'cadastrar_campo'),
    #path('cadastrar_atividade', AtividadeCreate.as_view(), name= 'cadastrar_atividade'),

]