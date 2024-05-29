from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.contrib import messages

 
from directorio.models import Situacion

# Create your views here.
class SituacionView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "directorio/situacion_list.html"
    login_url = 'config:home'
    model = Situacion
    permission_required = 'directorio:view_situacion'
    context_object_name = 'obj'
