from django.shortcuts import render
# from django.http import HttpResponse  # ya no se necesita, ya que se usa el template


# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("<h1> Bienvendio a Automart </h1")  # ya no se necesita, ya que se usa el template
