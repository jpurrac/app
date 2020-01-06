from django.urls import path, include
from .views import ProveedorView, ProveedorNew, ProveedorEdit

urlpatterns =[
    #PROVEEDORES
    path('proveedores/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'), #<int:pk>: recibe el id del registro que se modificara
   # path('categorias/delete/<int:pk>', CategoriaDelete.as_view(), name='categoria_del'),
]