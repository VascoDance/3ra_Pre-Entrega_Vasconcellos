from django import forms
from .models import Modelo1, Modelo2, Modelo3

class Modelo1Form(forms.ModelForm):
    class Meta:
        model = Modelo1
        fields = '__all__'

class Modelo2Form(forms.ModelForm):
    class Meta:
        model = Modelo2
        fields = '__all__'

class Modelo3Form(forms.ModelForm):
    class Meta:
        model = Modelo3
        fields = '__all__'