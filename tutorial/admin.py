from django.contrib import admin
from tutorial.models import Alumnos
# Register your models here.

@admin.register(Alumnos)
class Alumnos(admin.ModelAdmin):
    list_display = ('nombre','apellido','domicilio','telefono' )
    search_fields = ('apellido', 'id', 'nombre')
    pass
