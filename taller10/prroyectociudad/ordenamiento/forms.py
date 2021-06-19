from django.forms import ModelForm
from django import forms

from ordenamiento.models import Parroquia, \
    Barrio
        


class ParroquiaForm(ModelForm): 
    class Meta:
        model = Parroquia 
        fields = ['nombre', 'tipo'] 


class BarrioForm(ModelForm): 
    class Meta:
        model = Barrio 
        fields = ['nombre', 'número_viviendas', 'número_parques', 'limite_Parques',  'número_edificios'] 


class NumeroBarrioform(ModelForm): 
    
    def __init__(self, parroquia, *args, **kwargs):
        super(NumeroBarrioform, self).__init__(*args, **kwargs)
        self.initial['parroquia'] = parroquia
        self.fields["parroquia"].widget = forms.widgets.HiddenInput()
        print(Parroquia)
    
    class Meta:
        model = Barrio 
        fields = ['nombre', 'número_viviendas', 'número_parques', 'limite_Parques', 'número_edificios'] 


