from django.db import models

class Vaga(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    requisitos = models.TextField()
    jornada_trabalho = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
