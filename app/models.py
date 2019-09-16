from django.db import models

# Create your models here.
class Cliente(models.Model):
    rut = models.IntegerField('rut',  blank = False, null = False)
    nombre = models.CharField('Nombre', max_length=150, blank = False, null = False)
    correo = models.EmailField('Correo', max_length=255, blank = False, null = False)
    telefono = models.CharField('Telefono', max_length=10, blank = False, null = False)
    numero = models.IntegerField('Numero', blank = False, null = False)
    fecha_creacion =models.DateField("Fecha de creacion", auto_now=True, auto_now_add=False)
    fecha_modificacion =models.DateField("Fecha de modificacion",blank = True,null = True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre