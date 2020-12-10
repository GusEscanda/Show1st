from django.urls import path

from . import views
from mainApp.models import Page

urlpatterns = [
    path('',             views.showBlog, name = Page.BLOG),
    path('<int:pageId>', views.showBlog, name = Page.BLOG),
    path('addFilter/<int:pageId>/<str:addTagFilter>/<int:addDateFilter>',
            views.showBlog, name = Page.BLOG),
    path('addFilter/<int:pageId>//<int:addDateFilter>',
            views.showBlog, name = Page.BLOG),
]



