from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Persona(models.Model):
    PersonaId = models.IntegerField(primary_key=True, verbose_name='PersonaId')
    Rut = models.CharField(max_length=10, verbose_name='Rut')
    Nombre = models.CharField(max_length=20, verbose_name='Nombre')
    Paterno = models.CharField(max_length=20, verbose_name='Paterno')
    Materno = models.CharField(max_length=20, verbose_name='Materno')
	
    def __str__(self) -> str:
        return self.Nombre + ' ' + self.Paterno + ' ' + self.Materno


class Producto(models.Model):
    ProductoId = models.IntegerField(primary_key=True, verbose_name='ProductoId')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    imagen = models.ImageField(null=True, blank=True)
    Valor = models.FloatField()
    Stock = models.FloatField()

    def __str__(self) -> str:
        return self.nombre
@property
def imageURL(self):
	try:
		url = self.image.url
	except:
		url = ''
	return url

class Carrito(models.Model):
    CarritoId = models.IntegerField(primary_key=True, verbose_name='ProductoId')
    Total = models.IntegerField(verbose_name='Total')
    PersonaId = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Total

class DetalleCarrito(models.Model):
    DetalleCarritoId = models.IntegerField(primary_key=True, verbose_name='DetalleCarritoId')
    ProductoId = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad = models.IntegerField(verbose_name='Cantidad')

    def __str__(self) -> str:
        return self.Cantidad


class Carrito(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
	fecha = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaccion_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.cantidad for item in orderitems])
		return total


class OrderItem(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
	carrito = models.ForeignKey(Carrito, on_delete=models.SET_NULL, null=True)
	cantidad = models.IntegerField(default=0, null=True, blank=True)
	fecha = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.producto.precio * self.cantidad
		return total


class  pago (models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)
	carrito = models.ForeignKey(Carrito, on_delete=models.SET_NULL, null=True)
	direccion = models.CharField(max_length=200, null=False)
	ciudad = models.CharField(max_length=200, null=False)
	pais = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.direccion

class Cliente(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

