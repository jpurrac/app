from django.urls import path, include
from .views import ProveedorView, ProveedorNew, \
    ProveedorEdit, proveedorInactivar, ComprasView, ComprasDet, ComprasEnc, compras

urlpatterns =[
    #PROVEEDORES
    path('proveedores/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'), #<int:pk>: recibe el id del registro que se modificara
    path('proveedores/inactivar/<int:id>', proveedorInactivar, name="proveedor_inactivar"),

    path('compras/' , ComprasView.as_view(), name="compras_list"),
    path('compars/new', compras, name="compras_new"),
]