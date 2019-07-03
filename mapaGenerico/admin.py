from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from mapaGenerico.models import DatosGenerico


@admin.register(DatosGenerico)
class DatosAdmin(ImportExportModelAdmin):
    pass
