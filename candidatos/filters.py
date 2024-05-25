import django_filters

from .models import Candidato


class CandidatoFilter(django_filters.FilterSet):
    class Meta:
        model = Candidato
        fields = {
            "nome": ["icontains"],
            "educacao": ["icontains"],
            "nascimento": ["range"],
        }
