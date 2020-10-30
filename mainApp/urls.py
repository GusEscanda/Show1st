"""
Archivo urls.py especifico de la aplicacion. En caso de tener muchas aplicaciones y muchas urls, 
organizo poniendo las urls de cada app en un archivo propio y despues importo todos esos al urls.py general
del sitio
"""

from django.urls import path

from . import views

from django.conf import settings            # para incluir en urlpatterns las carpetas con las imagenes
from django.conf.urls.static import static  # para incluir en urlpatterns las carpetas con las imagenes

urlpatterns = [
    path('',                                        views.mainPage,      name='HOM'),
    path('<menuOpt>',                               views.mainPage,      name='HOM'),
    path('css/<str:sName>/<str:filename>.css',    views.cssRenderer),
    path('js/<str:filename>.js',                    views.jsRenderer),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




