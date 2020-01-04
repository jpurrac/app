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

class SubCategoria(ClaseModelo):

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría', #como placeholder
        unique= True
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.description,self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria,self).save()

    class Meta:
        verbose_name_plural = "Sub Categorias"
        unique_together = ('categoria', 'descripcion')

class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text="Descripcion de la Marca",
        unique= True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()
    
    class Meta:
        verbose_name_plural = "Marca"

class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text="Descripcion de la Unidad de Medida",
        unique= True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()
    
    class Meta:
        verbose_name_plural = "Unidades de Medida"

class Producto(ClaseModelo):
    codigo = models.CharField(
        max_length=20,
        unique=True
    )

    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida =models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria=models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()
    
    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo', 'codigo_barra')
