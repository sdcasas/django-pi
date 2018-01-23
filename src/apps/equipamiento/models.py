from django.db import models

# from apps.entidad import models as entidad
from apps.rrhh import models as rrhh


tab_disco = [0, 40, 80, 160, 300, 500, 640, 1024, 2048, 3072, 4096] #GB
tab_memoria = [0, 128, 256, 512, 1024, 1536, 2048, 2560, 3072, 4096, 8192, 16384] #MB
# tab_pulgadas = ['14','15','17','19', '20', '21', '22', '23', '24']
tab_pulgadas = (
    ('14', '14'),
    ('15', '15'),
)
tab_so = ['No posee','Windows XP', 'Windows Vista', 'Windows 7', 'Windows 8', 'Windows 10', 'Linux', 'Windows | Linux']
tab_unidad_optica = ['No Posee', 'CD-R', 'CD-RW', 'DVD-R', 'DVD-RW']
tab_estado = (
    ('MALO', 'Malo'),
    ('REGULAR', 'Regular'),
    ('BUENO', 'Bueno'),
    )


class Marca(models.Model):
    nombre = models.CharField(max_length=512)
    placa_madre = models.BooleanField()
    microprocesador = models.BooleanField()
    disco_rigido = models.BooleanField()
    memoria_ram = models.BooleanField()
    monitor = models.BooleanField()
    ups_estabilizador = models.BooleanField()
    placa_video = models.BooleanField()
    impresora = models.BooleanField()
    otro = models.BooleanField()

    def __str__(self):
        return self.nombre


class Impresora(models.Model):
    marca = models.ForeignKey(Marca, related_name="impresoras", on_delete=models.CASCADE)
    modelo = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    costo_aproximado = models.CharField(max_length=512, blank=True, null=True)
    conexion_red = models.CharField(max_length=512, blank=True, null=True)


class ImpresoraInsumo(models.Model):
    impresora = models.ForeignKey(Impresora, related_name="insumos", on_delete=models.CASCADE)
    tipo = models.CharField(max_length=512, blank=True, null=True)
    modelo = models.CharField(max_length=512, blank=True, null=True)
    color = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)


class Monitor(models.Model):

    tab_monitor_tipo = (
        ('CRT', 'CRT'),
        ('LCD', 'LCD'),
        ('LED', 'LED'),
        ('Plasma', 'Plasma')
    )

    marca = models.ForeignKey(Marca, related_name="monitores", on_delete=models.CASCADE)
    modelo = models.CharField(max_length=512, blank=True, null=True)
    pulgadas = models.CharField(max_length=512, choices=tab_pulgadas)
    tipo = models.CharField(max_length=512, choices=tab_monitor_tipo)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} {} {}"'.format(self.marca, self.modelo, self.pulgadas)

class Microprocesador(models.Model):
    marca = models.ForeignKey(Marca, related_name="microprocesadores", on_delete=models.CASCADE)
    modelo = models.CharField(max_length=512, blank=True, null=True)
    frecuencia_trabajo = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.CharField(max_length=512, blank=True, null=True)


class PlacaMadre(models.Model):
    marca = models.ForeignKey(Marca, related_name="placas_madre", on_delete=models.CASCADE)
    modelo = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.CharField(max_length=512, blank=True, null=True) 


class StockImpresora(models.Model):
    identificador = models.CharField(max_length=512, blank=True, null=True)
    impresora = models.ForeignKey(Impresora, related_name='stock', on_delete=models.CASCADE)
    responsable = models.ForeignKey(rrhh.Agente, 
        related_name="impresora_a_cargo", on_delete=models.CASCADE, 
        blank=True, null=True
        )
    area = models.ForeignKey(rrhh.Area, related_name='impresora_a_cargo', on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=tab_estado)
    nro_serie = models.CharField(max_length=512, blank=True, null=True)
    fecha_compra = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)


# class StockInsumo(models.Model):
#     nombre = models.CharField(max_length=512, blank=True, null=True)
#     descripcion = models.CharField(max_length=512, blank=True, null=True)
#     cant_min = models.CharField(max_length=512, blank=True, null=True)
#     cant_max = models.CharField(max_length=512, blank=True, null=True)
#     estado = models.CharField(max_length=512, blank=True, null=True)
#     stock_insumo_cat = models.ForeignKey('StockInsumoCat', models.DO_NOTHING, blank=True, null=True)
#     stock_insumo_cat_proveedor = models.ForeignKey('StockInsumoProveedor', models.DO_NOTHING, db_column='stock_insumo_cat_proveedor', blank=True, null=True)
#     fecha_compra = models.DateField(blank=True, null=True)
#     observaciones = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'stock_insumo'


# class StockInsumoCat(models.Model):
#     nombre = models.CharField(max_length=512, blank=True, null=True)
#     descripcion = models.CharField(max_length=512, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'stock_insumo_cat'


# class StockInsumoProveedor(models.Model):
#     nombre = models.CharField(max_length=512, blank=True, null=True)
#     descripcion = models.CharField(max_length=512, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'stock_insumo_proveedor'


class StockMonitor(models.Model):
    identificador = models.CharField(max_length=512, blank=True, null=True)
    monitor = models.ForeignKey(Monitor, related_name='stock', on_delete=models.CASCADE)
    responsable = models.ForeignKey(rrhh.Agente, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(rrhh.Area, models.DO_NOTHING)
    estado = models.CharField(max_length=20, choices=tab_estado)
    nro_serie = models.CharField(max_length=512, blank=True, null=True)
    fecha_compra = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    # def __str__(self):
        # return self.identificador
        # '{} {} {}"'.format(self.marca, self.modelo, self.pulgadas)


# class StockUpsEstabilizador(models.Model):
#     identificador = models.CharField(max_length=512, blank=True, null=True)
#     ups_estabilizador = models.ForeignKey(UpsEstabilizador, related_name='stock', on_delete=models.CASCADE)
#     responsable = models.ForeignKey(rrhh.Agente, models.DO_NOTHING, blank=True, null=True)
#     area = models.ForeignKey(rrhh.Area, models.DO_NOTHING, blank=True, null=True)
#     estado = models.CharField(max_length=512, blank=True, null=True)
#     nro_serie = models.CharField(max_length=512, blank=True, null=True)
#     fecha_compra = models.DateField(blank=True, null=True)
#     observaciones = models.TextField(blank=True, null=True)


class StockPC(models.Model):
    identificador = models.CharField(max_length=512, blank=True, null=True)
    microprocesador = models.ForeignKey(Microprocesador, 
        related_name="microprocesador", on_delete=models.CASCADE, blank=True, null=True)
    placa_madre = models.ForeignKey(PlacaMadre, 
        related_name="placa_madre", on_delete=models.CASCADE, blank=True, null=True)
    disco = models.CharField(max_length=512, blank=True, null=True)
    memoria = models.CharField(max_length=512, blank=True, null=True)
    so = models.CharField(max_length=512, blank=True, null=True)
    unidad_optica = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    area = models.ForeignKey(rrhh.Area, related_name='pc_a_cargo', on_delete=models.CASCADE)
    responsable = models.ForeignKey(rrhh.Agente, related_name='pc_a_cargo' , on_delete=models.CASCADE, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=tab_estado)