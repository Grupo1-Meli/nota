from django.shortcuts import render



from .models import *  

def tienda(request):
	productos = Producto.objects.all()
	context = {'productos':productos}
	return render(request, 'tienda/tienda.html', context)

def carrito(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'tienda/carrito.html', context)








def registro_c(request):
      context = {}
      return render(request, 'tienda/registro_c.html', context)