from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages

from bases.views import SinPrivilegios
from .models import Cliente, FacturaEnc, FacturaDet
from inv.models import Producto
from .forms import ClienteForm
import inv.views as inv


# Create your views here.
class ClienteView(SinPrivilegios, generic.ListView):

    model = Cliente
    template_name = "fac/cliente_list.html"
    context_object_name = "obj"
    permission_required = "cmp.view_cliente"

class VistaBaseCreate(SuccessMessageMixin, SinPrivilegios, generic.CreateView):

    context_object_name = 'obj'
    success_message = "Registro Agregado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class VistaBaseEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):

    context_object_name = 'obj'
    success_message = "Registro Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ClienteNew(VistaBaseCreate):
    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list")
    permission_required = "fac.add_cliente"


class ClienteEdit(VistaBaseEdit):
    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list")
    permission_required = "fac.change_cliente"

@login_required(login_url="/login/")
@permission_required("fac.change_cliente", login_url="/login/")
def clienteInactivar(request, id):
    cliente = Cliente.objects.filter(pk=id).first()

    if request.method == "POST":
        if cliente:
            cliente.estado = not cliente.estado
            cliente.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    return HttpResponse("FAIL")

class FacturaView(SinPrivilegios, generic.ListView):
    model = FacturaEnc #modelo el cual se trabaja   
    template_name = "fac/factura_list.html" #pagina en la cual mostrara al generar esta vista
    context_object_name = "obj" #nombre que le da al objeto, cuando existe algo en FacturaEnc?
    permission_required = "fac.view_facturaenc"

@login_required(login_url="/login/")
@permission_required("fac.change_facturaenc", login_url="bases:sin_privilegios")
def facturas(request, id=None): #se utiliza como vista | recibe el ID | ID se inicializa con NONE a menos, que se envie ID existente
    
    template_name='fac/facturas.html' #la info que se recopile, se enviara a esta pagina | SE DEVULVE EN EL RETURN AL FINAL DEL METODO
    detalle = {} #vacio | es info que se envia al template_name  | CONTEXTO
    clientes = Cliente.objects.filter(estado=True) # se guarda en variables, todos los clientes que existan, filtrandolos por estado TRUE | se manda info para template_name |CONTEXTO

    if  request.method == "GET": #SOLO PARA CUANDO SE VA A EDITAR Y DESPUES DE SE REDIRIGIDO POR UN POST| factura_edit
        enc = FacturaEnc.objects.filter(pk=id).first() #Se busca por el ID que se entrega por método, si existe un objeto, se entrega a la varialbe ENC

        if not enc: #de no encontrar un ENC (si es falso)
            encabezado = { # se le asigna como valor 0 y la fecha actual
                'id':0,
                'fecha':datetime.today(),
                'cliente':0,
                'sub_total':0.00,
                'descuento':0.00,
                'total':0.00
            } # SE MANDA DENTRO DEL CONTEXTO
            detalle=None #se va dentro del CONTEXTO 
        else: # si existe un enc en FacturaEnc | si enc es true
            encabezado = {
                'id':enc.id, #id se enviará dentro de encabezado, con alias enc, con el valor que se le da por id.enc(YA EXISTENTE EN LA BD), 
                #lo que se mostrara en el template_name. Esto se dará por JS al input correspondiente para mostrar
                'fecha':enc.fecha,#fecha = enc.fecha
                'cliente':enc.cliente,#cliente = enc.cliente | es ForeignKey del modelo Cliente
                'sub_total':enc.sub_total,# sub_total = enc.sub_total
                'descuento':enc.descuento,# descuento = enc.descuento
                'total':enc.total# total = enc.total
            }
            #si existe un enc, existe un detalle
            detalle = FacturaDet.objects.filter(factura=enc)  # se busca el detalle por por factura(enc= ID?)

        contexto = { "enc":encabezado, "det":detalle, "clientes":clientes} #Al editar (GET), en el contexto se agrega la informacion que se enviara al template_name(FACTURA.HTML) ...
        #se agrega el ENCABEZADO, el DETALLE del encabezado y los CLIENTES que existen en la BD

    #POST ocurre cuando el tag form, tiene el metodo POST 
    if request.method == "POST": # sucede cuando se le da al boton btnGuardar (boton submit)
        #lo que activa el metodo POST

        cliente = request.POST.get("enc_cliente") #rescata el valor que hay en el input enc_cliente y lo guarda como variable | se saca el valor del ID(numerico) del cliente (REVISAR EL HTML!!!)
        fecha = request.POST.get("fecha") # rescata el valor que hay en el input FECHA y lo guarda como variable

        cli = Cliente.objects.get(pk=cliente) #se guarda el cli el objeto cliente que se recupero del id cliente

        if not id: #si NO existe ID que se está enviando en el template por el metodo
            enc = FacturaEnc(
                cliente=cli, fecha= fecha
            )# las variables cliente y fecha, son enviaddos a enc(Modelo FacturaEnc). Crendo un nuevo enc
            if enc:# si existe enc (true)
                enc.save() #se guarda enc
                id = enc.id #id de ences igual a id, que se va al messagge error
        else: #Si el cliente existe, etnocens
            enc=FacturaEnc.objects.filter(pk=id).first() # se buscada en FacturaEnc(enc) el id
            if enc:
                enc.cliente = cli
                enc.save()
        
        if not id:
            messages.error(request, 'No puedo Continuar, No pude detectar No. Factura')
            return redirect("fac:factura_list")

        codigo = request.POST.get("codigo")
        cantidad = request.POST.get("cantidad")
        precio = request.POST.get("precio")
        s_total = request.POST.get("s_total")
        descuento = request.POST.get("descuento_detalle")
        total = request.POST.get("total_detalle")

        prod = Producto.objects.get(codigo=codigo)
        det= FacturaDet(
            factura= enc,
            producto = prod,
            cantidad = cantidad,
            precio = precio,
            sub_total = s_total,
            descuento = descuento,
            total = total
        )

        if det:
            det.save()

        return redirect("fac:factura_edit", id=id) #despues de guardar la informacion (POST), se redirige a factura_edit con el nuevo id que se asigno al nuevo objeto
        # DESPUES DE FINALIZAR EL POST, SE EJECUTA UN GET ENSEGUIDA
    return render(request, template_name, contexto)

class ProductoView(inv.ProductoView): #Hereda de PrudctoView de Intventario
    template_name = "fac/buscar_producto.html"

