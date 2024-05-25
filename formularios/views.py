from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Formulario
from vagas.models import Vaga
from .filters import FormularioFilter


def listaVagaCandidato(request, vaga_id):
    vaga = get_object_or_404(Vaga, pk=vaga_id)
    formularios = Formulario.objects.filter(vaga=vaga)
    formulario_filter = FormularioFilter(request.GET, formularios)
    return render(
        request,
        "formularios/formulario_list.html",
        {
            "formulario_list": formulario_filter.qs,
            "filter": formulario_filter,
            "vaga": vaga,
        },
    )


class FormularioCreateView(CreateView):
    model = Formulario
    fields = ["candidato", "vaga", "status"]

    def get_success_url(self):
        vaga_id = self.kwargs["vaga_id"]
        if vaga_id:
            return reverse("formulario_list", kwargs={"vaga_id": vaga_id})
        else:
            return reverse("home")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vaga_id"] = self.kwargs["vaga_id"]
        return context


class FormularioUpdateView(UpdateView):
    model = Formulario
    fields = ["candidato", "vaga", "status"]

    def get_success_url(self):
        vaga_id = self.kwargs["vaga_id"]
        return reverse("formulario_list", kwargs={"vaga_id": vaga_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vaga_id"] = self.kwargs["vaga_id"]
        return context


class FormularioDeleteView(DeleteView):
    model = Formulario

    def get_success_url(self):
        vaga_id = self.kwargs["vaga_id"]
        return reverse("formulario_list", kwargs={"vaga_id": vaga_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vaga_id"] = self.kwargs["vaga_id"]
        return context
