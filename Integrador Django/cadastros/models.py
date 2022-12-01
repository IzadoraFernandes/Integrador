from django.db import models

# Create your models here.

'''class Campo(models.Model):
    nome = models.CharField(max_length= 50 )
    descricao = models.CharField(max_length= 150, verbose_name="Descrição ") #verbose_name é utilizado para caracteres especiais.

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

class '''