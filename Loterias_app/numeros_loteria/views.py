from django.shortcuts import render
from numeros_loteria.models import NumeroLoteria
from numeros_loteria.models import datoslotos
# Create your views here.
def index(request):
    loterias = NumeroLoteria.devolver_numeros()
    context = {'loterias' : loterias}
    return render(request, 'index.html', context)


def slider(request):
    context = {}
    return render(request, 'slider.html', context)

