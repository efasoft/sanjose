from django.urls import path
from django.contrib.auth import views as auth_views

from bases.views import *

app_name = "config"

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('Inicio',Home.as_view(template_name='base/index.html'),name='inicio'),    
    path('login/',auth_views.LoginView.as_view(template_name='bases/login.html'),
        name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='bases/login.html'),
         name='logout'),
    path('sin_privilegios/',
         HomeSinPrivilegios.as_view(),
         name='sin_privilegios'), 


    
    path('users/lists',UserList.as_view(),name="users_list"),
    path('users/add',user_admin,name="user_add"),
    path('users/modify/<int:pk>',user_admin,name="user_modify"),
    path('users/groups/list',UserGroupList.as_view(),name="user_groups_list"),
    path('users/groups/add',user_groups_admin,name="user_groups_new"),
    path('users/groups/modify/<int:pk>',user_groups_admin,name="user_groups_modify"),
    path('users/groups/delete/<int:pk>',user_group_delete,name="user_groups_delete"),

    path('users/groups/permission/<int:id_grp>/<int:id_perm>',user_group_permission,name="user_groups_permission"),
    path('users/groups/admin/<int:id_usr>/<int:id_grp>',user_group_add,name="user_groups_admin"),

    path('staff_doc',Home.as_view(template_name='bases/staff_docentes.html'),name='staff_doc_uesj'),
    path('cursos',Home.as_view(template_name='bases/cursos_y_talleres.html'),name='cursos_y_talleres'),    
    path('actividades',Home.as_view(template_name='bases/proximas_actividades.html'),name='proximas_actividades'),   
    path('nuestro_blog',Home.as_view(template_name='bases/nuestro_blog.html'),name='nuestro_blog'),       
    path('catalogos/categorias',
	 Home.as_view(),
	 name='categorias'),
    path('catalogos/subcategorias',
        Home.as_view(),
        name='subcategorias'),
    path('movimientos/compras',
        Home.as_view(),
        name='compras'),       
]