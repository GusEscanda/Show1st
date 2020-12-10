from django.shortcuts import render

from mainApp.models import Page
from mainApp.views import getContextDict

from .models import InfoPage

# Create your views here.

def showInfo(request, pageId, subPageId=0):
    if subPageId:
        context = getContextDict( Page, InfoPage, subPageId )
        context['pageId'] = pageId
    else:
        context = getContextDict( Page, InfoPage, pageId )
    return render( request, "ShowInfo.html", context )




