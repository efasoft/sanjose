from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

 
from directorio.models import Condicion_Representante


# Create your views here.
class Condicion_RepresentanteView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "directorio/condicion_representante_list.html"
    login_url = 'config:home'
    model = Condicion_Representante
    permission_required = 'directorio:view_condicion_representante'
    context_object_name = 'obj'

@login_required(login_url='config:login')
@permission_required('directorio.change_condicion_representante', login_url='bases:login')

# IMPORTANTE VALIDAR QUE NO SE PUEDA INGRESAR SIN ESTAR LOGUEADO Y CON LOS PERMISOS, 
# AGREGA y MODIFICA UN REGISTRO
def condicion_representante_admin(request,pk=None):
    template_name = 'directorio/condicion_representante_add.html'
    context = {}
    descripcion = None    
    obj = Condicion_Representante.objects.filter(id = pk).first()
    context["obj"] = obj

    if request.method == "POST":
        # COLOCO EN MAYUSCULA LO INGRESADO EN EL FORM
        descripcion = request.POST.get("descripcion").upper() 
        grp = Condicion_Representante.objects.filter(descripcion=descripcion).first()

        # MUESTRO POR CONSOLA - NO ES NECESARIO
        print("ESTOY INGRESANDO *** : ",descripcion)
        print("---------------- grp : ",grp)        
        print("................  pk : ",pk)
  

        # VALIDANDO EL FORMULARIO
        # NO PUEDE QUEDAR EN BLANCO
        if not descripcion and pk == None: 
            # AGREGAR
            messages.error(request,"Por favor ingrese una Condición para el Representante")
            return redirect("direc:condicion_representante_new")
        elif not descripcion and pk != None:  
            # EDITAR
            messages.error(request,"ALERTA : Por favor ingrese una Condición para el Representante")  
            grp = Condicion_Representante.objects.filter(id=pk).first()                      
            return redirect("direc:condicion_representante_modify", grp.id)
        
        # NO PUEDE ESTAR DUPLICADO
        if grp and pk == None:
            messages.error(request,"Atención : Condicion del Representante ya existe, no puede volver a crearlo")
            return redirect("direc:condicion_representante_new")
        elif grp and grp.id != pk: 
            # EDITAR
            messages.error(request,"ALERTA : Condicion del Representante ya existe, no puede volver a crearlo")
            grp = Condicion_Representante.objects.filter(id=pk).first()                      
            return redirect("direc:condicion_representante_modify", grp.id)        

        
        if not grp and pk != None:
            # Condicion del Representante Existe, se está cambiando el dato registrado
            grp = Condicion_Representante.objects.filter(id=pk).first()
            grp.descripcion = descripcion
        elif not grp and pk == None:
            grp = Condicion_Representante(descripcion=descripcion)
        else:
            ...
        # SE PROCEDE A GRABAR EN LA TABLA
        grp.save()
        messages.success(request, "Registro Guardado Satisfactoriamente")
        return redirect('direc:condicion_representante_list')
    
    return render(request,template_name,context)

# ELIMINA UN REGISTRO
@login_required(login_url='config:login')
@permission_required('directorio.delete_condicion_representante', login_url='bases:login')
def condicion_representante_delete(request,pk):
    if request.method == "POST":
        grp = Condicion_Representante.objects.filter(id=pk).first()

        if not grp:
            print("Condicion de Representante No Existe")
        else:
            # SE PROCEDE A ELIMINAR DE LA TABLA
            grp.delete()
        
        messages.success(request,"Registro Borrado Satisfactoriamente")
        return HttpResponse("OK")    
