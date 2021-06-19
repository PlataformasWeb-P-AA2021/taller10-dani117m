from django.contrib import admin

# Register your models here.
from ordenamiento.models import Parroquia, Barrio
from import_export.admin import ImportExportModelAdmin

# Se crea una clase que hereda
# de ParroquiaAdmin para el modelo

class ParroquiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'tipo')
    


# el primer argumento es el modelo (Parroquia)
# el segundo argumento la clase ParroquiaAdmin
admin.site.register(Parroquia, ParroquiaAdmin)



# admin.site.register(BarrioAdmin)
class BarrioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'número_viviendas', 'número_parques', 'número_edificios')
    


admin.site.register(Barrio, BarrioAdmin)