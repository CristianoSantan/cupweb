from django.urls import path


from .views import (
    listaVagaCandidato,
    FormularioCreateView,
    FormularioUpdateView,
    FormularioDeleteView,
)

urlpatterns = [
    path("vagas/<int:vaga_id>/candidatos/", listaVagaCandidato, name="formulario_list"),
    path("vagas/<int:vaga_id>/create", FormularioCreateView.as_view(), name="formulario_create"),
    path(
        "vagas/<int:vaga_id>/update/<int:pk>",
        FormularioUpdateView.as_view(),
        name="formulario_update",
    ),
    path(
        "vagas/<int:vaga_id>/delete/<int:pk>",
        FormularioDeleteView.as_view(),
        name="formulario_delete",
    ),
]
