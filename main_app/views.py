from django.shortcuts import render
from .models import Auto
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
    autos = Auto.objects.all()
    return render(request, 'index.html', {'autos' : autos})

""" Eliminado para usar models.py
class Auto:
    def __init__(self, nombre, modelo, precio, color, img_url):
        self.nombre = nombre
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.img_url = img_url

autos = [
    Auto("VW Jetta", 2018, 145000, "Terracota", "https://soloautos.pxcrush.net/car/private/8lb3md6jngip2sbfd6zp5g0i6.jpg?pxc_method=gravityfill&pxc_size=720,480&pxc_bgtype=self"),
    Auto("Ibiza", 2017, 130000, "Blanco", "https://img.automexico.com/crop/535x349/2018/08/20/624f2eda-b-4a93.jpg"),
    Auto("Futura", 1955, 0, "Negro", "https://www.autoclasico.com.mx/Resources/Fotos/05/89/F05-0446789.jpg"),
    Auto("Ford", 1999, 35000, "Azul", "https://www.autosenreynosa.com/autos/img/larges/1524124161461.jpg")
] 
"""