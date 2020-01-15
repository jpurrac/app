from django.urls import path
from django.contrib.auth import views as auth_views
from bases.views import Home, HomeSinPrivilegios #Del directorio "bases", el archivo "views.py", la clase "HOME"



urlpatterns = [

    path('', Home.as_view(), name='home'), #Se finaliza con una coma
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bases/login.html'), name='logout'),
    path('sin_privilegios/', HomeSinPrivilegios.as_view(), name='sin_privilegios')
    ]