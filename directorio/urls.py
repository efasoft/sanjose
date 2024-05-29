from django.urls import path

from .views import SituacionView

app_name = "direc"

urlpatterns = [
    path('directorio/list',SituacionView.as_view(), name='situacion_list'),

]