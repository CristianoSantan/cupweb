from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Vaga


class VagaListView(ListView):
    model = Vaga


class VagaCreateView(CreateView):
    model = Vaga
    fields = ["titulo", "descricao", "requisitos", "jornada_trabalho", "salario"]
    success_url = reverse_lazy("vaga_list")


class VagaUpdateView(UpdateView):
    model = Vaga
    fields = ["titulo", "descricao", "requisitos", "jornada_trabalho", "salario"]
    success_url = reverse_lazy("vaga_list")


class VagaDeleteView(DeleteView):
    model = Vaga
    success_url = reverse_lazy("vaga_list")
