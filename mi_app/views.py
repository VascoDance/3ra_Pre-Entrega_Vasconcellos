from django.shortcuts import render
from django.views import View
from .forms import Modelo1Form, Modelo2Form, Modelo3Form
from .models import Modelo1, Modelo2, Modelo3

class FormularioView(View):
    def get(self, request):
        modelo1_form = Modelo1Form()
        modelo2_form = Modelo2Form()
        modelo3_form = Modelo3Form()
        return render(request, 'formulario.html', {'modelo1_form': modelo1_form, 'modelo2_form': modelo2_form, 'modelo3_form': modelo3_form})

    def post(self, request):
        
        pass

class BusquedaView(View):
    def get(self, request):
        
        pass

    from django.shortcuts import render
from django.views import View
from .forms import Modelo1Form, Modelo2Form, Modelo3Form
from .models import Modelo1, Modelo2, Modelo3

class FormularioView(View):
    def get(self, request):
        modelo1_form = Modelo1Form()
        modelo2_form = Modelo2Form()
        modelo3_form = Modelo3Form()
        return render(request, 'formulario.html', {'modelo1_form': modelo1_form, 'modelo2_form': modelo2_form, 'modelo3_form': modelo3_form})

    def post(self, request):
        # Manejar el envío de formularios aquí
        pass

class BusquedaView(View):
    def get(self, request):
        # Lógica para realizar la búsqueda en la base de datos
        return render(request, 'busqueda.html')