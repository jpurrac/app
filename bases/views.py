from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

#las clases comienzan con MAYUSCULA la primera letra
#se hereda de generic.TemplateView (vista)
class Home(LoginRequiredMixin,generic.TemplateView): #los mixin se ponene al lado izq, para mayor prioridad
    #la clase HOME hereda de lo que esta dentro del parentesis
    #template name, hace referencia a la plantilla que va a mostrar
    template_name = 'bases/home.html'
    login_url ='bases:login'

class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    template_name='bases/sin_privilegios.html'

class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = "bases:login"
    raise_exception = False #114
    redirect_field_name = "redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))