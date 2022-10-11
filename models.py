from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
 
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
 
class Caracteristica(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class  Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    telefono  = models.CharField(max_length=100)
    correo  = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    ruc = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
 
    def __str__(self):  
        return self.nombre+" - "+self.ruc+" - "+self.direccion

class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    estrella = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre+" - "+self.direccion+" - Estrellas: "+self.estrella

class Almacen(models.Model):  #falta editar
    nombre = models.CharField(max_length=100)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre+" - "+str(self.hotel)

class Producto(models.Model):
    codigo = models.CharField(max_length=25)
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre+" - "+str(self.marca)+" - "+str(self.categoria)

class ProductoCaracteristica(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    caracteristica = models.ForeignKey(Caracteristica, on_delete=models.CASCADE)
    valor = models.CharField(max_length=25)

    def __str__(self):
        return str(self.producto)+" - "+str(self.caracteristica)+" - S/. "+self.valor

class Compra(models.Model):
    comprobante = models.CharField(max_length=100)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    total= models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.comprobante+" - "+str(self.proveedor)

class CompraDetalles(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=12, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return str(self.compra)+" - "+str(self.producto)

#Ventas
class Venta(models.Model):
    comprobante = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total= models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.comprobante+" - "+str(self.cliente)
 
 
class VentaDetalles(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=12, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return str(self.compra)+" - "+str(self.producto)

class Inventario(models.Model):
    fechaHora = models.DateTimeField(auto_now_add=True)
    comprobante = models.CharField(max_length=100)
    compra_detalles = models.ForeignKey(CompraDetalles, on_delete=models.CASCADE)
    ventas_detalles = models.ForeignKey(VentaDetalles, on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    def __str__(self):
        return self.comprobante+" - "+str(self.almacen)
