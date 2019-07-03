from django.shortcuts import render

from tablib import Dataset

from mapaGenerico.resources import DatosResource


def simple_upload(request):
    if request.method == 'POST':
        datos_resource = DatosResource
        dataset = Dataset()
        new_datos = request.FILES['myfile']

        imported_data = dataset.load(new_datos.read())
        print('dataset: ' + str(dataset))
        print('new_datos: ' + str(new_datos))

        result = datos_resource.import_data(dataset, dry_run=True)  # Test the data import

        # if not result.has_errors():
        #   datos_resource.import_data(dataset, dry_run=False)  # Actually import now
        context = {
            'imported_data': imported_data,
        }
        return render(request, 'simple_upload.html', context=context)
