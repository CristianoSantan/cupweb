"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from home.views import index

from candidatos.views import (
    CandidatoListView,
    CandidatoCreateView,
    CandidatoUpdateView,
    CandidatoDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("lista_candidato", CandidatoListView.as_view(), name="candidato_list"),
    path("create", CandidatoCreateView.as_view(), name="candidato_create"),
    path("update/<int:pk>", CandidatoUpdateView.as_view(), name="candidato_update"),
    path("delete/<int:pk>", CandidatoDeleteView.as_view(), name="candidato_delete"),
]
