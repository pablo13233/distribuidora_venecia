from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', 
        admin.site.urls
    ),
    path('', 
        include('apps.home.urls'),
    ),
    path('', 
        include(('apps.categoria.urls'), namespace='categoria'),
    ),
    #path('', include('apps.carrusel.urls')),
    path('', include(('apps.producto.urls'), namespace='producto')),
    path('', include(('apps.marca.urls'), namespace='marca')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
