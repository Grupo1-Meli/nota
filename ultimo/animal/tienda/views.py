from django.shortcuts import render
from django.http import JsonResponse

import json
from .models import * 
from .forms import ProductoForm
from .forms import PersonaForm



from .models import *  

def editar(request):
	return render(request, 'panel/editar.html')

def cliente(request):
	personas=Persona.objects.all()
	datos={'personas': personas}
	return render(request, 'panel/cliente.html', datos)

def agregar(request):
    datos = {"form":ProductoForm()}
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto agregado!."
    return render(request, 'panel/agregar.html', datos)

def cli_agregar(request):
    datos = {"form":PersonaForm()}
    if request.method == "POST":
        form = PersonaForm(data=request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "C agregado!."
    return render(request, 'panel/cli_agregar.html', datos)

def index(request):
	productos=Producto.objects.all()
	datos={'productos': productos}
	return render(request, 'panel/index.html', datos)




def form(request):
	return render(request, 'admin/form.html')



def tienda(request):
	productos = Producto.objects.all()
	context = {'productos':productos}
	return render(request, 'tienda/tienda.html', context)

def tienda(request):
    
	if request.user.is_authenticated:
		cliente = request.user.cliente
		carrito, created = Carrito.objects.get_or_create(cliente=cliente, complete=False)
		items = carrito.orderitem_set.all()
		cartItems = carrito.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		carrito = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = carrito['get_cart_items']

	productos = Producto.objects.all()
	context = {'productos':productos, 'cartItems':cartItems}
	return render(request, 'tienda/tienda.html', context)







def carrito(request):

	if request.user.is_authenticated:
		cliente = request.user.cliente
		carrito, created = Carrito.objects.get_or_create(cliente=cliente, complete=False)
		items = carrito.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		carrito = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'carrito':carrito}
	return render(request, 'tienda/carrito.html', context)


def pago (request):
	if request.user.is_authenticated:
		cliente = request.user.cliente
		carrito, created = Carrito.objects.get_or_create(cliente=cliente, complete=False)
		items = carrito.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		carrito = {'get_cart_total':0, 'get_cart_items':0}


	context = {'items':items, 'carrito':carrito}
	return render(request, 'tienda/pago.html', context)




	
def updateItem(request):
	data = json.loads(request.body)
	productoId = data['productoId']
	action = data['action']

	
	print('Action:', action)
	print('ProductoId:', productoId)


	cliente = request.user.cliente
	producto = Producto.objects.get(id=productoId)
	carrito, created = Carrito.objects.get_or_create(carrito=carrito, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(carrito=carrito, producto=producto)

	if action == 'add':
		orderItem.cantidad = (orderItem.cantidad + 1)
	elif action == 'remove':
		orderItem.cantidad = (orderItem.cantidad - 1)

	orderItem.save()

	if orderItem.cantidad <= 0:
		orderItem.delete()


	return JsonResponse('Item was added', safe=False)





def pago (request):
      context = {}
      return render(request, 'tienda/pago.html', context)