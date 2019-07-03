from import_export import resources
from .models import DatosGenerico


class DatosResource(resources.ModelResource):
    class Meta:
        model = DatosGenerico
