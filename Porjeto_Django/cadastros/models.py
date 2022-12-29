from django.db import models
from django.urls import reverse_lazy


class Sala(models.Model):
    nome = models.CharField(max_length = 50)
    numero = models.IntegerField(verbose_name= "Número")
    bloco = models.CharField(max_length= 50, verbose_name="Bloco")

    def __str__(self):
        return "{} ({})".format(self.nome, self.bloco)

class Reserva(models.Model):
    nome = models.CharField(max_length=50)
    capacidade = models.IntegerField
    numero = models.IntegerField(verbose_name= "Número")
    bloco = models.IntegerField
    descricao = models.CharField(max_length= 200, verbose_name="Descrição")
    data = models.DateField(blank='False', null='False')

    Sala = models.ForeignKey(Sala, on_delete= models.PROTECT)

    #
    def __str__(self):
        return "{} ({})".format(self.nome, self.Sala)

class Laboratorio(models.Model):
    nome = models.CharField(max_length = 50)
    bloco = models.IntegerField
    descricao = models.CharField(max_length= 200, verbose_name="Descrição")


