from django.urls import path


from .views import (
    candidatoListView,
    CandidatoCreateView,
    CandidatoUpdateView,
    CandidatoDeleteView,
)

urlpatterns = [
    path("", candidatoListView, name="candidato_list"),
    path("create", CandidatoCreateView.as_view(), name="candidato_create"),
    path("update/<int:pk>", CandidatoUpdateView.as_view(), name="candidato_update"),
    path("delete/<int:pk>", CandidatoDeleteView.as_view(), name="candidato_delete"),
]