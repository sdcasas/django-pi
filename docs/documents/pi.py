# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agentes(models.Model):
    apellido = models.CharField(max_length=512, blank=True, null=True)
    nombres = models.CharField(max_length=512, blank=True, null=True)
    domicilio = models.CharField(max_length=512, blank=True, null=True)
    dni = models.CharField(max_length=512, blank=True, null=True)
    tel_coorporativo = models.CharField(max_length=512, blank=True, null=True)
    tel_celular = models.CharField(max_length=512, blank=True, null=True)
    tel_fijo = models.CharField(max_length=512, blank=True, null=True)
    area = models.ForeignKey('Areas', models.DO_NOTHING, blank=True, null=True)
    sexo = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agentes'


class Areas(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas'


class ImpresorasInsumos(models.Model):
    impresora = models.ForeignKey('TabImpresoras', models.DO_NOTHING, blank=True, null=True)
    tipo = models.CharField(max_length=512, blank=True, null=True)
    modelo = models.CharField(max_length=512, blank=True, null=True)
    color = models.CharField(db_column='Color', max_length=512, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impresoras_insumos'


class IpLan(models.Model):
    direccion_ip = models.CharField(max_length=45, blank=True, null=True)
    dispositivo_tipo = models.CharField(max_length=45, blank=True, null=True)
    mac = models.ForeignKey('Mac', models.DO_NOTHING, blank=True, null=True)
    dispositivo_id = models.CharField(max_length=512, blank=True, null=True)
    responsable = models.ForeignKey(Agentes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ip_lan'


class LibArticulos(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)
    stock_minimo = models.IntegerField(blank=True, null=True)
    stock_maximo = models.IntegerField(blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lib_articulos'


class LibEgresos(models.Model):
    fecha_entrega = models.DateField()
    agente = models.ForeignKey(Agentes, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)
    articulo = models.ForeignKey(LibArticulos, models.DO_NOTHING, blank=True, null=True)
    cantidad_entregada = models.IntegerField()
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lib_egresos'


class LibIngresos(models.Model):
    fecha_entrega = models.DateField()
    articulo = models.ForeignKey(LibArticulos, models.DO_NOTHING, blank=True, null=True)
    cantidad_recibida = models.IntegerField()
    observaciones = models.TextField(blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lib_ingresos'


class Mac(models.Model):
    dispositivo_tipo = models.CharField(max_length=512, blank=True, null=True)
    direccion_mac = models.CharField(max_length=512, blank=True, null=True)
    dispositivo_id = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mac'


class OtroDispo(models.Model):
    indicador = models.CharField(max_length=512, blank=True, null=True)
    dispositivo = models.CharField(max_length=512, blank=True, null=True)
    responsable = models.ForeignKey(Agentes, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)
    marca = models.ForeignKey('TabMarcas', models.DO_NOTHING, blank=True, null=True)
    modelo = models.CharField(max_length=512, blank=True, null=True)
    detalles = models.CharField(max_length=512, blank=True, null=True)
    estado = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otro_dispo'


class Pc(models.Model):
    identificador = models.CharField(max_length=512, blank=True, null=True)
    microprocesador = models.ForeignKey('TabMicroprocesadores', models.DO_NOTHING, blank=True, null=True)
    placa_madre = models.ForeignKey('TabPlacaMadre', models.DO_NOTHING, blank=True, null=True)
    disco = models.CharField(max_length=512, blank=True, null=True)
    memoria = models.CharField(max_length=512, blank=True, null=True)
    so = models.CharField(max_length=512, blank=True, null=True)
    unidad_optica = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)
    responsable = models.ForeignKey(Agentes, models.DO_NOTHING, blank=True, null=True)
    estado = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pc'


class Pedidos(models.Model):
    personal = models.ForeignKey(Agentes, models.DO_NOTHING, blank=True, null=True)
    fecha_solicitud = models.DateField()
    problema_tipo = models.CharField(max_length=512, blank=True, null=True)
    problema_detalle = models.TextField()
    problema_solucion_propuesta = models.TextField(blank=True, null=True)
    problema_estado = models.CharField(max_length=512, blank=True, null=True)
    personal_computos = models.ForeignKey(Agentes, models.DO_NOTHING, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    identificador = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'


class Portatiles(models.Model):
    responsable = models.ForeignKey(Agentes, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)
    tipo = models.CharField(max_length=512, blank=True, null=True)
    marca = models.ForeignKey('TabMarcas', models.DO_NOTHING, blank=True, null=True)
    modelo = models.CharField(max_length=512, blank=True, null=True)
    microprocesador = models.ForeignKey('TabMicroprocesadores', models.DO_NOTHING, blank=True, null=True)
    disco = models.CharField(max_length=512, blank=True, null=True)
    memoria = models.CharField(max_length=512, blank=True, null=True)
    pulgadas = models.CharField(max_length=512, blank=True, null=True)
    unidad_optica = models.CharField(max_length=512, blank=True, null=True)
    so = models.CharField(max_length=512, blank=True, null=True)
    propietario = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    identificador = models.CharField(max_length=512, blank=True, null=True)
    estado = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portatiles'


class SaaArticulos(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)
    stock_minimo = models.IntegerField(blank=True, null=True)
    stock_maximo = models.IntegerField(blank=True, null=True)
    categoria = models.ForeignKey('SaaCategorias', models.DO_NOTHING, blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saa_articulos'


class SaaCategorias(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saa_categorias'


class SaaEgresos(models.Model):
    fecha_entrega = models.DateField()
    agente = models.ForeignKey(Agentes, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)
    articulo = models.ForeignKey(SaaArticulos, models.DO_NOTHING, blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)
    cantidad_entregada = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'saa_egresos'


class SaaIngresos(models.Model):
    fecha_entrega = models.DateField()
    articulo = models.ForeignKey(SaaArticulos, models.DO_NOTHING, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)
    cantidad_recibida = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'saa_ingresos'


class SaaPedidosCompra(models.Model):
    fecha = models.DateField()
    articulo = models.ForeignKey(SaaArticulos, models.DO_NOTHING, blank=True, null=True)
    cantidad_pedida = models.IntegerField()
    observaciones = models.TextField(blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)
    estado = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saa_pedidos_compra'


class StockImpresoras(models.Model):
    identificador = models.CharField(max_length=512, blank=True, null=True)
    impresora = models.ForeignKey('TabImpresoras', models.DO_NOTHING, blank=True, null=True)
    responsable = models.ForeignKey(Agentes, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)
    estado = models.CharField(max_length=512, blank=True, null=True)
    nro_serie = models.CharField(max_length=512, blank=True, null=True)
    fecha_compra = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_impresoras'


class StockInsumo(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)
    descripcion = models.CharField(max_length=512, blank=True, null=True)
    cant_min = models.CharField(max_length=512, blank=True, null=True)
    cant_max = models.CharField(max_length=512, blank=True, null=True)
    estado = models.CharField(max_length=512, blank=True, null=True)
    stock_insumo_cat = models.ForeignKey('StockInsumoCat', models.DO_NOTHING, blank=True, null=True)
    stock_insumo_cat_proveedor = models.ForeignKey('StockInsumoProveedor', models.DO_NOTHING, db_column='stock_insumo_cat_proveedor', blank=True, null=True)
    fecha_compra = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_insumo'


class StockInsumoCat(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)
    descripcion = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_insumo_cat'


class StockInsumoProveedor(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)
    descripcion = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_insumo_proveedor'


class StockMonitores(models.Model):
    identificador = models.CharField(max_length=512, blank=True, null=True)
    monitor = models.ForeignKey('TabMonitores', models.DO_NOTHING, blank=True, null=True)
    responsable = models.ForeignKey(Agentes, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)
    estado = models.CharField(max_length=512, blank=True, null=True)
    nro_serie = models.CharField(max_length=512, blank=True, null=True)
    fecha_compra = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_monitores'


class StockUpsEstabilizador(models.Model):
    identificador = models.CharField(max_length=512, blank=True, null=True)
    ups_estabilizador = models.ForeignKey('TabUpsEstabilizador', models.DO_NOTHING, blank=True, null=True)
    responsable = models.ForeignKey(Agentes, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)
    estado = models.CharField(max_length=512, blank=True, null=True)
    nro_serie = models.CharField(max_length=512, blank=True, null=True)
    fecha_compra = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_ups_estabilizador'


class TabImpresoras(models.Model):
    marca = models.ForeignKey('TabMarcas', models.DO_NOTHING, blank=True, null=True)
    modelo = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    costo_aproximado = models.CharField(max_length=512, blank=True, null=True)
    conexion_red = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_impresoras'


class TabMarcas(models.Model):
    nombre = models.CharField(max_length=512)
    placa_madre = models.CharField(max_length=1, blank=True, null=True)
    microprocesador = models.CharField(max_length=1, blank=True, null=True)
    disco_rigido = models.CharField(max_length=1, blank=True, null=True)
    memoria_ram = models.CharField(max_length=1, blank=True, null=True)
    monitor = models.CharField(max_length=1, blank=True, null=True)
    ups_estabilizador = models.CharField(max_length=1, blank=True, null=True)
    placa_video = models.CharField(max_length=1, blank=True, null=True)
    impresora = models.CharField(max_length=1, blank=True, null=True)
    otro = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_marcas'


class Microprocesadores(models.Model):
    marca = models.ForeignKey(TabMarcas, models.DO_NOTHING, blank=True, null=True)
    modelo = models.CharField(max_length=512, blank=True, null=True)
    frecuencia_trabajo = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.CharField(max_length=512, blank=True, null=True)


class TabMonitores(models.Model):
    marca = models.ForeignKey(TabMarcas, models.DO_NOTHING, blank=True, null=True)
    modelo = models.CharField(max_length=512, blank=True, null=True)
    pulgadas = models.CharField(max_length=512, blank=True, null=True)
    tipo = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)


class TabPlacaMadre(models.Model):
    marca = models.ForeignKey(TabMarcas, models.DO_NOTHING, blank=True, null=True)
    modelo = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_placa_madre'


class TabUpsEstabilizador(models.Model):
    marca = models.ForeignKey(TabMarcas, models.DO_NOTHING, blank=True, null=True)
    modelo = models.CharField(max_length=512, blank=True, null=True)
    tipo = models.CharField(max_length=512, blank=True, null=True)
    potencia = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_ups_estabilizador'


class Telefonos(models.Model):
    numero = models.CharField(max_length=512, blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)
    referente = models.ForeignKey(Agentes, models.DO_NOTHING, db_column='referente', blank=True, null=True)
    num_externo = models.CharField(max_length=512, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefonos'
