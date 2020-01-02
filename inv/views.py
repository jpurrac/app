from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Categoria, SubCategoria
from .forms import CategoriaForm, SubCategoriaForm

# SE CREAN LAS VISTAS 

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


class CategoriaNew(LoginRequiredMixin, generic.CreateView): #CreateView, Django interpretara que se insertaran datos
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class= CategoriaForm
    success_url= reverse_lazy("inv:categoria_list")
    login_url = "bases:login"

    def form_valid(self, form): #video 64
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView): #CreateView, Django interpretara que se insertaran datos
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class= CategoriaForm
    success_url= reverse_lazy("inv:categoria_list")
    login_url = "bases:login"

    def form_valid(self, form): #video 68
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class CategoriaDelete(LoginRequiredMixin, generic.DeleteView): #CreateView, Django interpretara que se insertaran datos
    model = Categoria
    template_name = "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url= reverse_lazy("inv:categoria_list")

class SubCategoriaView(LoginRequiredMixin, generic.ListView):

    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"

class SubCategoriaNew(LoginRequiredMixin, generic.CreateView): #CreateView, Django interpretara que se insertaran datos
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class= SubCategoriaForm
    success_url= reverse_lazy("inv:subcategoria_list")
    login_url = "bases:login"

    def form_valid(self, form): #video 64
        form.instance.uc = self.request.user
        return super().form_valid(form)
