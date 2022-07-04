from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static

from django.conf import settings
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.tienda, name="tienda"),
	path('carrito/', views.carrito, name="carrito"),
	path('pago/', views.pago, name="pago"),

	
	path('editar', views.editar, name="editar"),
	path('agregar', views.agregar, name="agregar"),
	path('cli_agregar', views.cli_agregar, name="cli_agregar"),
	path('index', views.index, name="index"),
	path('form', views.form, name="form"),
	path('update_item/', views.updateItem, name="update_item"),
	path('cliente', views.cliente, name="cliente"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)