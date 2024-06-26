from django.contrib import admin
from django.urls import path, include
from home.views import index


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("candidatos/", include("candidatos.urls")),
    path("vagas/", include("vagas.urls")),
    path("formularios/", include("formularios.urls"))
]
