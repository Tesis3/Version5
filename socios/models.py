from django.db import models
from django.utils import timezone
from inicio.models import ClaseModelo
# Create your models here.

class Socio(ClaseModelo):
    nombre = models.CharField(
        max_length=100,
        help_text='Nombre del Socio'
    )

    apellido = models.CharField(
        max_length=100,
        help_text='Apellido del Socio'
    )

    email = models.CharField(
        max_length=100,
        help_text='Email del Socio'
    )

    telefono = models.CharField(
        max_length=100,
        help_text='Telefono del Socio'
    )

    fecha_nacimiento = models.DateField()

    dni =models.CharField(
        max_length=15,
        help_text='DNI del Socio',
        unique=True
    )

    fecha_creacion = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return '{}'.format(self.dni)
    
    def save(self):
        self.nombre = self.nombre.title()
        self.apellido = self.apellido.title()
        self.email = self.email.lower()
        super(Socio,self).save()

    class Meta:
        verbose_name_plural = "Socios"