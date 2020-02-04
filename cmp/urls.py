from django.urls import path, include
from .views import ProveedorView, ProveedorNew, \
    ProveedorEdit, proveedorInactivar, ComprasView, \
    ComprasDet, ComprasEnc, compras, CompraDetDelete

from .reportes import reporte_compras

urlpatterns =[
    #PROVEEDORES
    path('proveedores/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'), #<int:pk>: recibe el id del registro que se modificara
    path('proveedores/inactivar/<int:id>', proveedorInactivar, name="proveedor_inactivar"),

    path('compras/' , ComprasView.as_view(), name="compras_list"),
    path('compras/new', compras, name="compras_new"),
    path('compras/edit/<int:compra_id>' , compras, name="compras_edit"),
    path('compras/<int:compra_id>/delete/<int:pk>' , CompraDetDelete.as_view(), name="compras_del"),

    path('compras/listado', reporte_compras, name='compras_print_all'),
]