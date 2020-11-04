"""
Archivo urls.py especifico de la aplicacion. En caso de tener muchas aplicaciones y muchas urls, 
organizo poniendo las urls de cada app en un archivo propio y despues importo todos esos al urls.py general
del sitio
"""

from django.urls import path

from . import views
from mainApp.models import MenuOption

from django.conf import settings            # para incluir en urlpatterns las carpetas con las imagenes
from django.conf.urls.static import static  # para incluir en urlpatterns las carpetas con las imagenes

urlpatterns = [
    path('',                               views.showInfo,   name=MenuOption.INFO),
    path('<menuOpt>',                      views.showInfo,   name=MenuOption.INFO),
    path('infoPage/<menuOpt>/<infoPage>',  views.showInfo,   name=MenuOption.INFO),
]



