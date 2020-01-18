from django.db import models

from bases.models import ClaseModelo

class Proveedor(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        unique=True
    )
    direccion = models.CharField(
        max_length=250,
        null=True, 
        blank=True
    )
    contacto = models.CharField(
        max_length=100
    )
    telefono=models.CharField(
        max_length=10,
        null=True, 
        blank=True
    )
    email=models.CharField(
        max_length=250,
        null=True, 
        blank=True 
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural = "Proveedores"

    class ComprasEnc(ClaseModelo):
        fecha_compra = models.DataField(null=True, blank=True)
        descripcion = models.TextField(null=True, blank= True)
        no_factura = models.CharField(null=True, blank= True)
        fecha_factura = models.DateField()
        sub_total = models.FloatField(default=0)
        descuento = models.FloatField(default=0)
        total = models.FloatField(default=0)

        proveedor = models.ForeignKey(Proveedor., on_delete=models.CASCADE) #investigar esta linea

        def __str__(self):
            return self.'{}'.format(self.observacion)
        
        def save(self):
            self.observacion  = self.observacion.upper()
            self.total = self.sub_total - self.descuento #se hace una resta
            super(ComprasEnc, self).save() #121 video, cachar de nuevo

        class Meta:
            verbose_name_plural = "Encabezado Compras"
            verbose_name = "Encabezado Compras"

    class ComprasDel(ClaseModelo):
        compra = models.ForeignKey(ComprasEnc, on_delete=models.CASCADE)
        producto = models.ForeignKey(producto, on_delete=models.CASCADE) 
        fecha_compra = models.DataField(null=True, blank=True)
        descripcion = models.TextField(null=True, blank= True)
        no_factura = models.CharField(null=True, blank= True)
        fecha_factura = models.DateField()
        sub_total = models.FloatField(default=0)
        descuento = models.FloatField(default=0)
        total = models.FloatField(default=0)

        proveedor = models.ForeignKey(Proveedor., on_delete=models.CASCADE) #investigar esta linea

        def __str__(self):
            return self.'{}'.format(self.observacion)