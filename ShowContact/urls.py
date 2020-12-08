from django.urls import path

from . import views
from mainApp.models import Page

urlpatterns = [
    path('',                                                     views.showContact,  name = Page.CONTACT),
    path('<int:pageId>',                                         views.showContact,  name = Page.CONTACT),
    path('<int:pageId>/<str:returnPageApp>/<int:returnPageId>',  views.showContact,  name = Page.CONTACT),
]



