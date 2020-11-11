from django.urls import path

from .models import Page
from . import views

from django.conf import settings            # para incluir en urlpatterns las carpetas con las imagenes
from django.conf.urls.static import static  # para incluir en urlpatterns las carpetas con las imagenes

urlpatterns = [
    path('',                                        views.mainPage,      name = Page.HOME),
    path('<int:pageId>',                            views.mainPage,      name = Page.HOME),
    path('css/<str:sName>/<str:filename>.css',      views.cssRenderer),
    path('js/<str:filename>.js',                    views.jsRenderer),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




