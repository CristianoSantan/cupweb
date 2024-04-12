from django.db import models

from candidatos.models import Candidato
from vagas.models import Vaga

class Formulario(models.Model):
    id_formulario = models.AutoField(primary_key=True)
    data_preenchimento = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('Enviado', 'Enviado'),
        ('Em Análise', 'Em Análise'),
        ('Aprovado', 'Aprovado'),
        ('Rejeitado', 'Rejeitado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
