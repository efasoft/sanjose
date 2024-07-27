from django.urls import path

from .views import *

app_name = "direc"

urlpatterns = [
    path('directorio/lists',Condicion_RepresentanteView.as_view(), name='condicion_representante_list'),
    path('directorio/add',condicion_representante_admin,name="condicion_representante_new"),
    path('directorio/modify/<int:pk>',condicion_representante_admin,name="condicion_representante_modify"),
    path('directorio/delete/<int:pk>',condicion_representante_delete,name="condicion_representante_delete"),    



]