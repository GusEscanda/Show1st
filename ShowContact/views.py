from django.shortcuts import render

from mainApp.models import Page
from mainApp.views import getContextDict

from .models import ContactPage, ContactChannel
from .forms import ContactForm

# Create your views here.

def showContact(request, pageId):
    context = getContextDict( Page, ContactPage, pageId )
    context['form'] = ContactForm()
    context['channels'] = ContactChannel.objects.all().order_by('order')
    return render( request, "ShowContact.html", context )




