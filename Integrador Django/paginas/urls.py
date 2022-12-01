from django.urls import path
# o . na frente significa que estou pegando algo que foi criado dentro do projeto
from .views import IndexView, SobreView, LoginView, CriarusuarioView, InformaticaView, ApiculturaView, AlimentosView, QuimicaView, MinhasreservasView, CriarnovolabView, CriarnovasalaView
#from . import views
#views.index

urlpatterns = [
         #endereço,  minhaView.as_view(), nome da url
    path('', IndexView.as_view(), name='inicio'), #para projetos grandes colocar: paginas-index
    #path('', views.index, name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('login/', LoginView.as_view(), name='login'),
    path('cadastro/', CriarusuarioView.as_view(), name='cadastro'),
    path('informática/', InformaticaView.as_view(), name='informática'),
    path('alimentos/', AlimentosView.as_view(), name='alimentos'),
    path('apicultura/', ApiculturaView.as_view(), name='apicultura'),
    path('quimica/', QuimicaView.as_view(), name='quimica'),
    path('novolab/', CriarnovolabView.as_view(), name='laboratorio'),
    path('minhasreservas/', MinhasreservasView.as_view(), name='reservas'),
    path('novasala/', CriarnovasalaView.as_view(), name='sala'),
    

]