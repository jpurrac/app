from django.db import models

from bases.models import ClaseModelo
# Create your models here.
class Cliente(ClaseModelo):
    NAT = 'Natural'
    JUR = 'Jurídica'
    TIPO_CLIENTE = [
        (NAT, 'Natural'),
        (JUR, 'Jurídica')
    ]
    nombres = models.CharField(
        max_length=100
    )
    apellidos = models.CharField(
        max_length=100
    )
    celular = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    tipo = models.CharField( #Django hará una especie de Spinner
        max_length=10,
        choices=TIPO_CLIENTE,
        default=NAT
    )
    def __str__(self):
        return '{} {}'.format(self.apellidos,self.nombres) #cuando se hjaga referencia al cliente, concatenara el no,mbre y apellido
    
    def save(self):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Cliente,self).save()

    class Meta:
        verbose_name_plural: "Clientes"