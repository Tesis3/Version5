from django.db import models

# Create your models here.

class ClaseModelo(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_fin = models.DateTimeField(auto_now=False,null=True,blank=True)

    class Meta:
        abstract=True