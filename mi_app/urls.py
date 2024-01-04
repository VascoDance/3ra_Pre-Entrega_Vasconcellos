from django.urls import path
from .views import FormularioView, BusquedaView

urlpatterns = [
    path('formulario/', FormularioView.as_view(), name='formulario'),
    path('busqueda/', BusquedaView.as_view(), name='busqueda'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_app/', include('mi_app.urls')),
]