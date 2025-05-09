from django.db import models

from bases.models import ClaseModelo

# USANDO PYDANTIC
from pydantic import BaseModel, Field, EmailStr, validator
from datetime import date, datetime
from typing import Optional
import re

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


# USANDO PYDANTIC

#class UserFormModel(BaseModel):
#    nombres: str = Field(max_length=60, min_length=1, error_messages={"max_length": "El nombre no puede exceder los 60 caracteres", "min_length": "El nombre no puede estar vacío"})
#    apellidos: str = Field(..., max_length=60, error_msg="El campo apellidos no debe exceder 60 caracteres")
##    edad: int = Field(gt=0, le=100, error_messages={"gt": "La edad debe ser mayor a 0", "le": "La edad no puede ser mayor a 100"})
#    fecha: Field(alias="fecha_nacimiento", format='%d-%m-%Y', error_messages={"format": "La fecha debe tener el formato DD-MM-AAAA"})
#    email: str = Field(regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", error_messages={"regex": "Ingrese un correo electrónico válido"})

#
#    @validator('fecha')
#    def check_fecha(cls, v):
#        min_fecha = date.today().replace(year=date.today().year - 100)
##        if v < min_fecha:
#            raise ValueError("La fecha no debe ser menor a 100 años de la fecha actual")
#        return v



 