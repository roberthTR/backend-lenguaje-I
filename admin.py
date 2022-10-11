from xml.parsers.expat import model
from django.contrib import admin

from.import models

# Register your models here.


admin.site.register(models.Marca)
admin.site.register(models.Categoria)
admin.site.register(models.Caracteristica)
admin.site.register(models.Cliente)
admin.site.register(models.Proveedor)
admin.site.register(models.Hotel)
admin.site.register(models.Almacen)
admin.site.register(models.Producto)
admin.site.register(models.ProductoCaracteristica)
admin.site.register(models.Compra)
admin.site.register(models.CompraDetalles)
admin.site.register(models.Venta)
admin.site.register(models.VentaDetalles)
admin.site.register(models.Inventario)
