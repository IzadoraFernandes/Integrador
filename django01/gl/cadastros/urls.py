from django.urls import path


from .views import SalaCreate, ReservaCreate, SalaUpdate, ReservaUpdate
urlpatterns = [
    path('cadastrar/sala/', SalaCreate.as_view(), name= 'cadastrar-sala'),
    path('cadastrar/reserva/', ReservaCreate.as_view(), name= 'cadastrar-reserva'),

    path('editar/sala <int:pk>', SalaUpdate.as_view(), name= 'editar-sala'),
    path('editar/reserva <int:pk>', ReservaUpdate.as_view(), name= 'editar-reserva'),

]


