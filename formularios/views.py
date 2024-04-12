from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Formulario


class FormularioListView(ListView):
    model = Formulario


class FormularioCreateView(CreateView):
    model = Formulario
    fields = ["candidato", "vaga", "status"]
    success_url = reverse_lazy("formulario_list")


class FormularioUpdateView(UpdateView):
    model = Formulario
    fields = ["candidato", "vaga", "status"]
    success_url = reverse_lazy("formulario_list")


class FormularioDeleteView(DeleteView):
    model = Formulario
    success_url = reverse_lazy("formulario_list")
