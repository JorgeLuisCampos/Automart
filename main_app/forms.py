from django import forms
from .models import Auto

""" Se sustituye por la clase de abajo
lass AutoForm(forms.Form):
  nombre = forms.CharField(label='Nombre', max_length=100)
  precio = forms.DecimalField(label='Precio', max_digits=10, decimal_places=2)
  modelo = forms.CharField(label='Modelo', max_length=4)
  color = forms.CharField(label='Color', max_length=100)
  img_url = forms.CharField(label='URL de Imagen')
"""

class AutoForm(forms.ModelForm):
  class Meta:
    model = Auto
    fields = ['nombre', 'precio', 'modelo', 'color', 'img_url']