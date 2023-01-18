from django.urls import path
#from . import views
from .views import  CadastrarReservaView, CadastrarSalaView, SalasListView , ReservaListView, ReservaUpdateView,ReservaDeleteView, SalasListView, SalasUpdateView
urlpatterns = [
    
    #path('cadastrar_lab/', Cadastrar_labView.as_view(), name = 'cadastrar_lab'),
    path('cadastrar_reserva/', CadastrarReservaView.as_view(), name = 'cadastrar_reserva'),
    path('cadastrar_sala/', CadastrarSalaView.as_view(), name = 'cadastrar_sala'),
    path('salas/', SalasListView.as_view(), name = 'salas'),
    path('teste/', ReservaListView.as_view(), name = 'teste'),
    path('<int:pk>/update/', ReservaUpdateView.as_view(), name='update-reserva'),
    path('<int:pk>/delete/', ReservaDeleteView.as_view(), name='delete-reserva'),
    path('<int:pk>/update/', SalasUpdateView.as_view(), name='update-salas'),

]
