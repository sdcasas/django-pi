from django.db import models


class Area(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Agente(models.Model):
    apellido = models.CharField(max_length=512, blank=True, null=True)
    nombres = models.CharField(max_length=512, blank=True, null=True)
    domicilio = models.CharField(max_length=512, blank=True, null=True)
    dni = models.CharField(max_length=512, blank=True, null=True)
    tel_coorporativo = models.CharField(max_length=512, blank=True, null=True)
    tel_celular = models.CharField(max_length=512, blank=True, null=True)
    tel_fijo = models.CharField(max_length=512, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    sexo = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.apellido, self.nombre)