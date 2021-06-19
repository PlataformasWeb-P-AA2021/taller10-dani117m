from django import forms
from django.db import models

# Creacion de tabla parroquia
class Parroquia(models.Model):
    class Meta: 
        ordering = ["tipo", "nombre"]
        verbose_name_plural = "La Parroquias"
    # se ordena por tipo de parroquia 
    tipo_parroquia = (
        # segun se lee el csv se usara como tipo Parroquia Urbana o Parroquia rural
        ('urbano','Parroquia Urbana' ),
        ('rural', 'Parroquia Rural'),
        )

    nombre = models.CharField(max_length=30)

    tipo = models.CharField(max_length=30, \
            choices=tipo_parroquia) 


    def __str__(self):
        return "%s - %s " % (self.nombre, 
                self.tipo)
# Creacion de tabla barrio 
class Barrio(models.Model):
    """
    """
    nombre = models.CharField(max_length=50)
    número_viviendas = models.IntegerField()
    limite_Parques = (
        (0, 'Ninguno'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        )
    número_parques = models.IntegerField(choices=limite_Parques)
    número_edificios = models.IntegerField()
    # parroquia se crea como llave foreanea se enlaza parroquia 
    parroquia = models.ForeignKey(Parroquia, related_name='lasparroquias', on_delete=models.CASCADE)
    def __str__(self):
        return "Matricula: %s-%s-%s-%s-%s " % \
                (self.nombre, 
                self.número_viviendas,
                self.número_parques,
                self.número_edificios,
                self.parroquia)