from django.shortcuts import render
from .models import Auto
# from django.http import HttpResponse  # ya no se necesita, ya que se usa el template

# Create your views here.
def index(request):
    # return render(request,'index.html')   # eliminado para mandar el diccionario con datos
    # return HttpResponse("<h1> Bienvendio a Automart </h1")  # ya no se necesita, ya que se usa el template
    autos = Auto.objects.all()
    return render(request, 'index.html', {'autos' : autos})

def show(request, auto_id):
    auto = Auto.objects.get(id=auto_id)
    return render(request, 'show.html', {'auto' : auto})