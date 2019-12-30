from django.db import models

from bases.models import ClaseModelo #SE IMPORTA LA CLASE

class Categoria(ClaseModelo):
    descripcion= models.CharField( #propiedades del atributo
        max_length=100,
        help_text='Descripción de la Categoría', #como placeholder
        unique= True
    )

    def __str__(self): #__str__ retorna un string
        return '{}'.format(self.descripcion) #se reemplazara el nombre de la categoria en '{}'


    def save(self):
        self.descripcion = self.descripcion.upper() #la descripcion se guardara en MAYUSCULA
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorias"