from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
import json

from .models import Proveedor
from .forms import ProveedorForm
from bases.views import SinPrivilegios

class ProveedorView(SinPrivilegios, generic.ListView):

    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    permission_required = "cmp.view_proveedor"


class ProveedorNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView): #CreateView, Django interpretara que se insertaran datos
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class= ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_list")
    permission_required = "cmp.add_proveedor"
    success_message="Proveedor Creado Satisfactoriamente"

    def form_valid(self, form): #video 64
        form.instance.uc = self.request.user
        print(self.request.user.id)
        return super().form_valid(form)

class ProveedorEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView): #CreateView, Django interpretara que se insertaran datos
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class= ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_list")
    success_message="Proveedor Actualizada Satisfactoriamente"
    permission_required = "cmp.change_proveedor"


    def form_valid(self, form): #video 68
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)
        
@login_required(login_url='/login/')#117
@permission_required('inv.change_proveedor', login_url='bases:sin_privilegios')
def proveedorInactivar(request, id):
    template_name='cmp/proveedor_inact.html'
    contexto = {}
    prv = Proveedor.objects.filter(pk=id).first()

    if not prv :
        return  HttpResponse('Proveedor NO existe' + str(id))
    
    if request.method == 'GET':
        contexto = {'obj': prv}

    if request.method == 'POST':
        prv.estado = False
        prv.save()
        contexto={'obj':'OK'}
        return HttpResponse('Proveedor Inactivado')

    return render(request, template_name,contexto)
