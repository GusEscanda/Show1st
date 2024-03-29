from django.urls import path

from . import views
from mainApp.models import Page

urlpatterns = [
    path('',                                           views.showItems,   name = Page.ITEMS),
    path('<int:pageId>',                               views.showItems,   name = Page.ITEMS),
    path('addFilter/<int:pageId>/<str:addCatFilter>',  views.showItems,   name = Page.ITEMS),
    path('updateCart',                                 views.updateCart),
    path('resetCart',                                  views.resetCart),
]



