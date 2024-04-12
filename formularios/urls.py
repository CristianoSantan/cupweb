from django.urls import path


from .views import (
    FormularioListView,
    FormularioCreateView,
    FormularioUpdateView,
    FormularioDeleteView,
)

urlpatterns = [
    path("", FormularioListView.as_view(), name="formulario_list"),
    path("create", FormularioCreateView.as_view(), name="formulario_create"),
    path("update/<int:pk>", FormularioUpdateView.as_view(), name="formulario_update"),
    path("delete/<int:pk>", FormularioDeleteView.as_view(), name="formulario_delete"),
]