# <!-- Ult. Act. 15/08/2024 -->
from django.http.response import Http404, HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.contrib import messages

from .models import Usuario
from .forms import Userform

# Create your views here.
class AjaxableResponseMixin:    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response


class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin, AjaxableResponseMixin):
    login_url = 'config:login'    
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='config:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class inicio(TemplateView):
    # Se llama a la pagina inicio.. Sin Loguearse
    # Para controlar que se haga primero el Login, se debe agregar 
    # en la Clase - LoginRequiredMixin y el url
    # login_url = 'config:login'
    template_name = 'base/index.html'

class Home(TemplateView):
    # Se llama a la pagina inicio.. Sin Loguearse
    # Para controlar que se haga primero el Login, se debe agregar 
    # en la Clase - LoginRequiredMixin y el url
    # login_url = 'config:login'
    template_name = 'bases/home.html'

class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "config:login"
    template_name="bases/sin_privilegios.html"



class UserList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "bases/users_list.html"
    login_url = 'config:login'
    model = Usuario
    permission_required = 'bases:view_usuario'
    context_object_name = 'obj'

# USUARIOS / PERMISOS
@login_required(login_url='config:login')
@permission_required('bases.change_ususario', login_url='config:home')
def user_admin(request,pk=None):
    template_name = "bases/users_add.html"
    context = {}
    form = None
    obj = None

    # MUESTRO LOS DATOS DENTRO DEL FORMULARIO PARA AGREGAR O EDITAR
    if request.method == "GET":
        if not pk:
            form = Userform(instance = None )
        else:
            obj = Usuario.objects.filter(id=pk).first()
            form = Userform(instance = obj)
        context["form"] = form
        context["obj"] = obj

        grupos_usuarios = None
        grupos = None
        if obj:
            grupos_usuarios = obj.groups.all()
            grupos = Group.objects.filter(~Q(id__in=obj.groups.values('id')))
        
        context["grupos_usuario"]=grupos_usuarios
        context["grupos"]=grupos
    
    # OBTEBGO LOS DATOS DEL FORMULARIO PARA AGREGAR O EDITAR
    if request.method == "POST":
        # COLOCO EN VARIABLES LOS DATOS DEL FORM
        data = request.POST
        e = data.get("email")
        fn = data.get("first_name")
        ln = data.get("last_name")
        p = data.get("password")

       # VALIDANDO EL FORMULARIO
        # NO PUEDE QUEDAR EN BLANCO
        ## EMAIL ##
        if not e and pk == None: 
            # AGREGAR
            messages.error(request,"Por favor ingrese una Dirección de Email")
            return redirect("config:user_add")
        elif not e and pk != None:  
            # EDITAR
            messages.error(request,"ALERTA : Por favor ingrese una Dirección de Email")  
            obj = Usuario.objects.filter(id=pk).first()                      
            return redirect("config:user_modify", obj.id)
        ## NOMBRES ##
        if not fn and pk == None: 
            # AGREGAR
            messages.error(request,"Por favor ingrese los Nombres")
            return redirect("config:user_add")
        elif not fn and pk != None:  
            # EDITAR
            messages.error(request,"ALERTA : Por favor ingrese los Nombres")  
            obj = Usuario.objects.filter(id=pk).first()                      
            return redirect("config:user_modify", obj.id)
        ## APELLIDOS ##
        if not ln and pk == None: 
            # AGREGAR
            messages.error(request,"Por favor ingrese los Apellidos")
            return redirect("config:user_add")
        elif not ln and pk != None:  
            # EDITAR
            messages.error(request,"ALERTA : Por favor ingrese los Apellidos")  
            obj = Usuario.objects.filter(id=pk).first()                      
            return redirect("config:user_modify", obj.id)        
        ## PASSWORD ##
        if not p and pk == None: 
            # AGREGAR
            messages.error(request,"Por favor ingrese el Password")
            return redirect("config:user_add")
        elif not p and pk != None:  
            # EDITAR
            messages.error(request,"ALERTA : Por favor ingrese el Password")  
            obj = Usuario.objects.filter(id=pk).first()                      
            return redirect("config:user_modify", obj.id)   
        
        # NO PUEDE REPETIR ESTE CAMPO EN OTRO REGISTRO
        ## EMAIL ##



        if pk:
            obj = Usuario.objects.filter(id=pk).first()
            if not obj:
                print("Error Usuario No Existe")
            else:
                obj.email = e
                obj.first_name = fn
                obj.last_name = ln
                obj.password = make_password(p)
                obj.save()
        else:
            obj = Usuario.objects.create_user(
                email = e,
                password = p,
                first_name = fn,
                last_name = ln
            )
            print(obj.email,obj.password)
        return redirect('config:users_list')
    
    return render(request,template_name,context)
#
"""
    if request.method == "POST":
        # COLOCO EN MAYUSCULA LO INGRESADO EN EL FORM
        descripcion = request.POST.get("descripcion").upper() 
        grp = Condicion_Alumno.objects.filter(descripcion=descripcion).first()

       # VALIDANDO EL FORMULARIO
        # NO PUEDE QUEDAR EN BLANCO
        if not descripcion and pk == None: 
            # AGREGAR
            messages.error(request,"Por favor ingrese una Condición para el Alumno")
            return redirect("direc:condicion_alumno_new")
        elif not descripcion and pk != None:  
            # EDITAR
            messages.error(request,"ALERTA : Por favor ingrese una Condición para el Alumno")  
            grp = Condicion_Alumno.objects.filter(id=pk).first()                      
            return redirect("direc:condicion_alumno_modify", grp.id)
        
        # NO PUEDE ESTAR DUPLICADO
        if grp and pk == None:
            messages.error(request,"Atención : Condicion del Alumno ya existe, no puede volver a crearlo")
            return redirect("direc:condicion_alumno_new")
        elif grp and grp.id != pk: 
            # EDITAR
            messages.error(request,"ALERTA : Condicion del Alumno ya existe, no puede volver a crearlo")
            grp = Condicion_Alumno.objects.filter(id=pk).first()                      
            return redirect("direc:condicion_alumno_modify", grp.id)        

        
        if not grp and pk != None:
            # Condicion del Alumno Existe, se está cambiando el dato registrado
            grp = Condicion_Alumno.objects.filter(id=pk).first()
            grp.descripcion = descripcion
        elif not grp and pk == None:
            grp = Condicion_Alumno(descripcion=descripcion)
        else:
            ...
        # SE PROCEDE A GRABAR EN LA TABLA
        grp.save()
        messages.success(request, "Registro Guardado Satisfactoriamente")
        return redirect('direc:condicion_alumno_list')
    
    return render(request,template_name,context)
"""
#










class UserGroupList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "bases/users_group_list.html"
    login_url = 'config:login'
    model = Group
    permission_required = 'bases:view_usuario'
    context_object_name = 'obj'

@login_required(login_url='config:login')
@permission_required('bases.change_usuario', login_url='bases:login')
def user_groups_admin(request,pk=None):
    template_name = 'bases/users_group_add.html'
    context = {}

    obj = Group.objects.filter(id = pk).first()
    context["obj"] = obj
    permisos = {}
    permisos_grupo = {}
    context["permisos"] = permisos
    context["permisos_grupo"] = permisos_grupo

    if obj:
        permisos_grupo = obj.permissions.all()
        context["permisos_grupo"] = permisos_grupo

        permisos = Permission.objects.filter(~Q(group=obj))
        context["permisos"] = permisos

    # print(permisos)
    # print(permisos_grupo)
    if request.method == "POST":
        name = request.POST.get("name")
        grp = Group.objects.filter(name=name).first()

        if grp and grp.id != pk:
            print("Grupo ya existe, no puede volver a crearlo")
            messages.error(request,"Grupo ya existe, no puede volver a crearlo")
            return redirect("config:user_groups_new")
        
        if not grp and pk != None:
            # Grupo Existe, se está cambiando el Nombre
            grp = Group.objects.filter(id=pk).first()
            grp.name = name
        elif not grp and pk == None:
            grp = Group(name=name)
        else:
            ...
        
        grp.save()
        messages.success(request, "Registro Guardado Satisfactoriamente")
        return redirect("config:user_groups_modify", grp.id)
    return render(request,template_name,context)

@login_required(login_url='config:login')
@permission_required('bases.change_usuario', login_url='bases:login')
def user_group_delete(request,pk):
    if request.method == "POST":
        grp = Group.objects.filter(id=pk).first()

        if not grp:
            print("Grupo No Existe")
        else:
            grp.delete()
        
        messages.success(request,"Registro Borrado Satisfactoriamente")
        return HttpResponse("OK")

@login_required(login_url='config:login')
@permission_required('bases.change_usuario', login_url='bases:login')
def user_group_permission(request,id_grp,id_perm):
    if request.method == "POST":
        grp = Group.objects.filter(id = id_grp).first()

        if not grp:
            messages.error(request,"Grupo No Existe")
            return HttpResponse("Grupo No Existe")
        
        accion = request.POST.get("accion")
        perm = Permission.objects.filter(id=id_perm).first()
        if not perm:
            messages.error(request,"Permiso no existe")
            return HttpResponse("Permiso No Existe")
        
        if accion == "ADD":
            grp.permissions.add(perm)
            messages.success(request,"Permiso Agregado")
        elif accion == "DEL":
            grp.permissions.remove(perm)
            messages.warning(request,"Permiso Eliminado")
        else:
            messages.error(request,"Accion no Reconocida")
            return HttpResponse("Accion No Reconocida")

        return HttpResponse("OK")
    return Http404("Método no Reconocido")


@login_required(login_url='config:login')
@permission_required('bases.change_usuario', login_url='bases:login')
def user_group_add(request,id_usr,id_grp):
    if request.method == "POST":
        usr =Usuario.objects.filter(id=id_usr).first()
        if not usr:
            messages.error(request,"Usuario No Existe")
            return HttpResponse("Usuario NO Existe")
        
        accion = request.POST.get("accion")
        grp = Group.objects.filter(id=id_grp).first()

        if not grp:
            messages.error(request,"Grupo no existe")
            return HttpResponse("Grupo No Existe")
        
        if accion=="ADD":
            usr.groups.add(grp)
            messages.success(request,"Grupo Agregado")
        elif accion=="DEL":
            usr.groups.remove(grp)
            messages.warning(request,"Grupo Eliminado")
        else:
            messages.error(request,"Accion no Reconocida")
            return HttpResponse("Acción no Reconocida")
        
        return HttpResponse("OK")
    
    return HttpResponse("Error Método no Reconocido")

    

        
