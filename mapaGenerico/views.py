import csv
import io

from django.contrib import messages
from django.shortcuts import render

from tablib import Dataset

from mapaGenerico.models import DatosGenerico
from mapaGenerico.resources import DatosResource


def upload(request):
    template = 'simple_upload.html'
    context = {}
    if request.method == 'GET':
        return render(request, template, context)

    csv_file = request.FILES['file']

    '''
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'el fichero no es un csv')
    '''
    print('name: ' + csv_file.name)
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='"'):
        _, created = DatosGenerico.objects.update_or_create(
            nombre=column[0],
            descripcion=column[1],
            latitud=column[2],
            longitud=column[3],
        )
    context = {}
    return render(request, template, context)


def mapa(request):
    return render(request, 'mapa.html', context={})
