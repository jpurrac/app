from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

#las clases comienzan con MAYUSCULA la primera letra
#se hereda de generic.TemplateView (vista)
class Home(LoginRequiredMixin,generic.TemplateView): #los mixin se ponene al lado izq, para mayor prioridad
    #la clase HOME hereda de lo que esta dentro del parentesis
    #template name, hace referencia a la plantilla que va a mostrar
    template_name = 'bases/home.html'
    login_url ='/admin'

