from django.urls import path
from . import views 
from django.conf import settings 
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('mapas', views.mapas, name='mapas'),
    path('subir', views.subir_pedido, name='subir'),
    path('editar', views.editar, name='editar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
