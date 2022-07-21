from django.db import models
from inicio.models import ClaseModelo

class Segmento(ClaseModelo):
    nombre = models.CharField(
        max_length=100,
        help_text='Descripcion del Segmento',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Segmento,self).save()

    class Meta:
        verbose_name_plural = "Segmentos"

class Marca(ClaseModelo):
    nombre = models.CharField(
        max_length=100,
        help_text='Descripcion de la Marca',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Marca,self).save()

    class Meta:
        verbose_name_plural = "Marcas"        

class Rubro(ClaseModelo):
    nombre = models.CharField(
        max_length=100,
        help_text='Descripcion del Rubro',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Rubro,self).save()

    class Meta:
        verbose_name_plural = "Rubros"  

class Producto(ClaseModelo):
    rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE)
    segmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(
        max_length=100,
        help_text='Descripcion del Producto'
    )

    def __str__(self):
        return '{} {} {} {}'.format(self.rubro.nombre,self.segmento.nombre,self.marca.nombre,self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Producto,self).save()

    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('rubro','segmento','marca','nombre')  

class Stock(ClaseModelo):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)        
    volumen = models.IntegerField()

class Precio(ClaseModelo):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)        
    moneda = models.CharField(
        max_length=50,
        help_text='Tipo de Moneda (USD/ARS)'
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)