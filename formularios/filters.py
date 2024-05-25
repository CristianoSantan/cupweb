import django_filters

from .models import Formulario


class FormularioFilter(django_filters.FilterSet):
    class Meta:
        model = Formulario
        fields = {
            "candidato__nome": ["icontains"],
            "candidato__educacao": ["icontains"],
            "candidato__endereco": ["icontains"],
            "candidato__experiencia_profissional": ["icontains"],
            "status": ["icontains"],
        }