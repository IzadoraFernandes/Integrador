from django.db import models
from django.urls import reverse_lazy


class Sala(models.Model):
    nome = models.CharField(max_length = 50)
    descricao = models.CharField(max_length= 200, verbose_name="Descrição")

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

class Reserva(models.Model):
    nome = models.CharField(max_length=50)
    capacidade = models.IntegerField
    numero = models.IntegerField(verbose_name= "Número")
    bloco = models.IntegerField
    descricao = models.CharField(max_length= 200, verbose_name="Descrição")

    Sala = models.ForeignKey(Sala, on_delete= models.PROTECT)

    #
    def __str__(self):
        return "{} ({})".format(self.nome, self.Sala)


