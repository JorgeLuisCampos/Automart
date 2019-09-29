from django.shortcuts import render
from django.http import HttpResponseRedirect  # ya no se necesita, ya que se usa el template # Ahora siempre sí
from .models import Auto
from .forms import AutoForm
from django_user_agents.utils import get_user_agent


# Create your views here.
def index(request):
    # return render(request,'index.html')   # eliminado para mandar el diccionario con datos
    # return HttpResponse("<h1> Bienvendio a Automart </h1")  # ya no se necesita, ya que se usa el template
    autos = Auto.objects.all()
    form = AutoForm()
    return render(request, 'index.html', {'autos' : autos, 'form' : form})

def show(request, auto_id):
    auto = Auto.objects.get(id=auto_id)
    ua = get_user_agent(request)
    return render(request, 'show.html', {'auto' : auto, 'user_agent': ua})

def post_auto(request):
    form = AutoForm(request.POST)
    if form.is_valid():
        """ Se cambia por form.save()
        auto = Auto(nombre = form.cleaned_data['nombre'],
                    precio = form.cleaned_data['precio'], 
                    modelo = form.cleaned_data['modelo'], 
                    color = form.cleaned_data['color'],
                    img_url = form.cleaned_data['img_url'])
        auto.save()
        """
        form.save(commit = True)
    return HttpResponseRedirect('/')