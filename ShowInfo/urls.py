from django.urls import path

from . import views
from mainApp.models import Page

urlpatterns = [
    path('',                                       views.showInfo,   name = Page.INFO),
    path('<int:pageId>',                           views.showInfo,   name = Page.INFO),
    path('infoPage/<int:pageId>/<int:subPageId>',  views.showInfo,   name = Page.INFO),
]

