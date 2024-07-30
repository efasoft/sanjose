from django.urls import path

from .views import *

app_name = "direc"

urlpatterns = [
    # CONDICION DE LOS REPRESENTANTES
    path('directorio/lists',Condicion_RepresentanteView.as_view(), name='condicion_representante_list'),
    path('directorio/add',condicion_representante_admin,name="condicion_representante_new"),
    path('directorio/modify/<int:pk>',condicion_representante_admin,name="condicion_representante_modify"),
    path('directorio/delete/<int:pk>',condicion_representante_delete,name="condicion_representante_delete"),    
    # CONDICION DE LOS ALUMNOS
    path('alumnos/list',Condicion_AlumnoView.as_view(), name='condicion_alumno_list'),
    path('alumnos/add',condicion_alumno_admin,name="condicion_alumno_new"),
    path('alumnos/modify/<int:pk>',condicion_alumno_admin,name="condicion_alumno_modify"),
    path('alumnos/delete/<int:pk>',condicion_alumno_delete,name="condicion_alumno_delete"),    


]