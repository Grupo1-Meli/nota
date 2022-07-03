from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.tienda, name="tienda"),
	path('carrito/', views.carrito, name="carrito"),
	path('registro_c/', views.registro_c, name="registro_c"),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)