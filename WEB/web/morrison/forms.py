from django import forms 
from .models import Mapa
 
class MapaForm(forms.ModelForm):
    class Meta:
        model = Mapa
        fields = '__all__'

