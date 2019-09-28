from django import forms


class AutoForm(forms.Form):
  nombre = forms.CharField(label='Nombre', max_length=100)
  precio = forms.DecimalField(label='Precio', max_digits=10, decimal_places=2)
  modelo = forms.CharField(label='Modelo', max_length=4)
  color = forms.CharField(label='Color', max_length=100)
  img_url = forms.CharField(label='URL de Imagen')