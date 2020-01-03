from django.urls import path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDelete, SubCategoriaView,SubCategoriaNew, SubCategoriaEdit, SubCategoriaDelete, MarcaView, MarcaNew, MarcaEdit, marca_inactivar


urlpatterns =[
    #CATEGORIA
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'), #<int:pk>: recibe el id del registro que se modificara
    path('categorias/delete/<int:pk>', CategoriaDelete.as_view(), name='categoria_del'),

    #SUBCATEGORIA
    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>', SubCategoriaDelete.as_view(), name='subcategoria_del'),

    #MARCA
    path('marcas/', MarcaView.as_view(), name='marca_list'),
    path('marcas/new', MarcaNew.as_view(), name='marca_new'),
    path('marcas/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
    path('marcas/inactivar/<int:id>', marca_inactivar , name='marca_inactivar'),
]