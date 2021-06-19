"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('listabarrios/<int:id>', views.obtener_barrios, 
            name='obtener_barrios'),
        path('crear/parroquia', views.crear_parroquia, 
            name='crear_parroquia'),
        path('editar_parroquia/<int:id>', views.editar_parroquia, 
            name='editar_parroquia'),
        path('crear/barrio', views.crear_barrio, 
            name='crear_barrio'),
        path('editar_barrio/<int:id>', views.editar_barrio, 
            name='editar_barrio'),
        
        
 ]
