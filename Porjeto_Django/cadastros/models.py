from django.db import models
from django.urls import reverse_lazy
#from braces.views import GroupRequiredMixin
import datetime 
from usuario.models import CustomUser

class Sala( models.Model):
    #group_required = u"Coapac"
    tipo = models.CharField(max_length=50) 
    nome = models.CharField(max_length = 250, unique=True)
    numero = models.IntegerField(verbose_name= "Número", unique=True)
    bloco = models.CharField(max_length= 10, verbose_name="Bloco")
    descricao = models.TextField(max_length= 100, verbose_name="Descrição")
    capacidade = models.IntegerField(verbose_name= "Capacidade")
    laboratorio = models.BooleanField(verbose_name= "É laboratório?", default=False)
    
    def __str__(self):
        return "{} ({})".format(self.nome, self.bloco)


class Reserva(models.Model):

    HORARIOS = (
        ('07:00 - 07:45', '07:00 - 07:45'),
        ('07:45 - 08:30', '07:45 - 08:30'),
        ('08:50 - 09:35', '08:50 - 09:35'),
        ('09:35 - 10:20', '09:35 - 10:20'),
        ('10:30 - 11:15', '10:30 - 11:15'),
        ('11:15 - 12:00', '11:15 - 12:00'),

        ('13:00 - 13:45', '13:00 - 13:45'),
        ('13:45 - 14:30', '13:45 - 14:30'),
        ('14:50 - 15:35', '14:50 - 15:35'),
        ('15:35 - 16:20', '15:35 - 16:20'),
        ('16:30 - 17:15', '16:30 - 17:15'),
        ('17:15 - 18:00', '17:15 - 18:00'),

        ('19:00 - 19:45', '19:00 - 19:45'),
        ('19:45 - 20:30', '19:45 - 20:30'),
        ('20:40 - 21:25', '20:40 - 21:25'),
        ('21:25 - 22:10', '21:25 - 22:10'),
    )
   
    #group_required = u"Professores"

    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length= 100, verbose_name="Descrição", blank=True)
    data = models.DateField(blank='False', null='False')
      
    horario = models.CharField(max_length=15, choices= HORARIOS)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    #usuario = models.ForeignKey(CustomUser, on_delete= models.CASCADE)

            
    def __str__(self):
        return "{} ({})".format(self.nome, self.data)