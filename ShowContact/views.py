from django.shortcuts import render

from mainApp.models import Page
from mainApp.views import getContextDict

from .models import ContactPage

# Create your views here.

def showContact(request, pageId):
    return render( request, "ShowContact.html", getContextDict( Page, ContactPage, pageId ) )




