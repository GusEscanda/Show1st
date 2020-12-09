from django.shortcuts import render

from .models import Page, Style, HomePage

# Create your views here.

def getContextDict(pages, appPages, pageId):
    # Obtain the basic data that shares all the apps (menu structure, pageId, page object)
    menuOptions = pages.objects.filter( location__in = (Page.NAVBAR,Page.FOOTER) ).order_by('position')
    if not pageId:
        pageId = menuOptions[0].id
    page = appPages.objects.get( id = pageId )
    return { 'menuOptions': menuOptions, 'pageId': pageId, 'page': page }


def homePage(request, pageId = ''):
    return render( request, "homePage.html", getContextDict(Page,HomePage,pageId) )


def cssRenderer(request, sName, filename):
    dictionary = {}
    if sName:
        dictionary['style'] = Style.objects.get( name = sName )
    return render(request, 'css/' + filename + '.css', dictionary, content_type="text/css")


def jsRenderer(request, filename):
    return render(request, 'js/' + filename + '.js', {}, content_type="text/javascript")

