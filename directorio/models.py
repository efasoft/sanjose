from django.db import models

from bases.models import ClaseModelo

# DIRECTORIO - MODELOS
class Condicion_Representante(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Condición del Representante',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Condicion_Representante, self).save()

    class Meta:
        verbose_name_plural = "Condicion_Representante"

class Condicion_Alumno(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Condición del Alumno',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Condicion_Alumno, self).save()

    class Meta:
        verbose_name_plural = "Condicion_Alumno"        
 