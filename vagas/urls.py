from django.urls import path


from .views import (
    VagaListView,
    VagaCreateView,
    VagaUpdateView,
    VagaDeleteView,
)

urlpatterns = [
    path("", VagaListView.as_view(), name="vaga_list"),
    path("create", VagaCreateView.as_view(), name="vaga_create"),
    path("update/<int:pk>", VagaUpdateView.as_view(), name="vaga_update"),
    path("delete/<int:pk>", VagaDeleteView.as_view(), name="vaga_delete"),
]