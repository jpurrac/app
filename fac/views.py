from django.shortcuts import render
from django.views import generic

from bases.views import SinPrivilegios
from .models import Cliente
from .forms import ClienteForm


# Create your views here.
class ClienteView(SinPrivilegios, generic.ListView):

    model = Cliente
    template_name = "fac/cliente_list.html"
    context_object_name = "obj"
    permission_required = "cmp.view_cliente"
