from django.urls import path
from bases.views import Home #Del directorio "bases", el archivo "views.py", la clase "HOME"

urlpatterns = [

    path('', Home.as_view(), name='home'), #Se finaliza con una coma

]