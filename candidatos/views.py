from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Candidato


class CandidatoListView(ListView):
    model = Candidato


class CandidatoCreateView(CreateView):
    model = Candidato
    fields = ["nome", "email", "endereco", "telefone", "educacao", "nascimento", "experiencia_profissional"]
    success_url = reverse_lazy("candidato_list")


class CandidatoUpdateView(UpdateView):
    model = Candidato
    fields = ["nome", "email", "endereco", "telefone", "educacao", "nascimento", "experiencia_profissional"]
    success_url = reverse_lazy("candidato_list")


class CandidatoDeleteView(DeleteView):
    model = Candidato
    success_url = reverse_lazy("candidato_list")

