from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render

from .models import Candidato
from .filters import CandidatoFilter


def candidatoListView(request):
    candidatos = Candidato.objects
    candidato_filter = CandidatoFilter(request.GET, candidatos)
    return render(
        request,
        "candidatos/candidato_list.html",
        {"candidato_list": candidato_filter.qs, "filter": candidato_filter},
    )


class CandidatoCreateView(CreateView):
    model = Candidato
    fields = [
        "nome",
        "email",
        "endereco",
        "telefone",
        "educacao",
        "nascimento",
        "experiencia_profissional",
    ]
    success_url = reverse_lazy("candidato_list")


class CandidatoUpdateView(UpdateView):
    model = Candidato
    fields = [
        "nome",
        "email",
        "endereco",
        "telefone",
        "educacao",
        "nascimento",
        "experiencia_profissional",
    ]
    success_url = reverse_lazy("candidato_list")


class CandidatoDeleteView(DeleteView):
    model = Candidato
    success_url = reverse_lazy("candidato_list")
