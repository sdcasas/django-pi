from django.contrib import admin

from . import models


admin.site.register(models.Marca)
admin.site.register(models.Monitor)
admin.site.register(models.Impresora)
admin.site.register(models.Microprocesador)
admin.site.register(models.PlacaMadre)

admin.site.register(models.StockPC)
admin.site.register(models.StockMonitor)
admin.site.register(models.StockImpresora)