from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

class ClaseModelo(models.Model):
    #variables de la clase
    estado = models.BooleanField(default=True) #estado
    fc = models.DateTimeField(auto_now_add=True) #fecha creacion, se agregará automaticamente
    fm = models.DateTimeField(auto_now=True) # fehcamodificacion
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null = True)

    #Se le dice a Djgango, que no tome en cuenta el modelo al emigrar
    class Meta:
        abstract = True

class ClaseModelo2(models.Model):
    estado = models.BooleanField(default=True) #estado
    fc = models.DateTimeField(auto_now_add=True) #fecha creacion, se agregará automaticamente
    fm = models.DateTimeField(auto_now=True) # fehcamodificacion
   # uc = models.ForeignKey(User, on_delete=models.CASCADE)
   # um = models.IntegerField(blank=True, null = True)
    uc = UserForeignKey(auto_user_add=True, related_name='+')
    um = UserForeignKey(auto_user=True, related_name='+')

    class Meta:
        abstract = True