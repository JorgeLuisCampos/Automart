from django.shortcuts import render
# from django.http import HttpResponse  # ya no se necesita, ya que se usa el template


# Create your views here.
def index(request):
    # return render(request,'index.html')   # eliminado para mandar el diccionario con datos
    # return HttpResponse("<h1> Bienvendio a Automart </h1")  # ya no se necesita, ya que se usa el template

    """ Ya no se ocupa este contexto al crear la clase de Autos y la lista de autos
    nombre = "VW Jetta"
    modelo = 2018
    precio = 145000
    color = "Terracota"

    contexto = {'auto_nombre' : nombre,
     'auto_modelo' : modelo,
     'auto_precio' : precio,
     'auto_color' : color
    }
    """

    return render(request, 'index.html', {'autos' : autos})

class Auto:
    def __init__(self, nombre, modelo, precio, color):
        self.nombre = nombre
        self.modelo = modelo
        self.precio = precio
        self.color = color

autos = [
    Auto("VW Jetta", 2018, 145000, "Terracota"),
    Auto("Ibiza", 2017, 130000, "Blanco"),
    Auto("Futura", 1955, 0, "Azul plata"),
    Auto("Ford", 1999, 35000, "Negro")
] 
