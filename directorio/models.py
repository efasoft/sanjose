from django.db import models

from bases.models import ClaseModelo

# Create your models here.
class Situacion(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Situación del Representante',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Situacion, self).save()

    class Meta:
        verbose_name_plural = "Situacion"
