from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripcion de la Categoria", 'estado':"Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs): #*args, puede tomar una cantidad indefinida de argumentos
        super().__init__(*args, **kwargs) #**kargs diccionario que contiene el nombre de cada uno de los argumentos junto con su valor
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })