from django.shortcuts import render

from lolcito.models import Fondo

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def fondo(request):
    fondo = Fondo.objects.all()
    return render(request, 'paginas/inicio.html', {'fondo': fondo})

