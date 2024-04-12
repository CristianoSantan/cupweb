from datetime import date

from django.db import models

class Candidato(models.Model):
    nome = models.CharField(max_length=80, null=False, blank=False)
    endereco = models.CharField(max_length=80, null=False, blank=False)
    email = models.CharField(max_length=80, null=False, blank=False)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    educacao = models.CharField(max_length=255, null=False, blank=False)
    experiencia_profissional = models.CharField(verbose_name="experiência profissional",max_length=255, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)


    class Meta:
        ordering = ["nome"]
