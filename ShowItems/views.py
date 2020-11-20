from django.shortcuts import render
from django.http import HttpResponse

from mainApp.models import Page, Prueba
from mainApp.views import getContextDict

from .models import ItemsPage, ItemCategory, Item

# Create your views here.

def showItems(request, pageId, addFilter=''):
    contextDict = getContextDict( Page, ItemsPage, pageId )
    # Obtain the items, optionally filtered by pageFilter
    pageFilter = contextDict['page'].pageFilter
    if pageFilter:
        myItems = Item.objects.filter( itemCats = pageFilter ).order_by('itemCode')
        catFiltered = pageFilter.catName
    else:
        myItems = Item.objects.all().order_by('itemCode')
        catFiltered = ''
    # Obtain a list (without duplicates) of ALL the tags that appear in any of the MENU FILTERED items
    allCats = []
    for item in myItems:
        for cat in item.itemCats.all():
            if cat.catName not in allCats and cat.catName != catFiltered:
                allCats.append( cat.catName )
    # Make the additional filtering
    filter = addFilter
    if filter:
        filter = [ f.strip() for f in filter.split(',') ] # convert the string into a list
        myItems = myItems.filter( itemCats__catName__in = filter ).order_by('itemCode')
    # Complete the context dictionary
    contextDict['items'] = myItems
    contextDict['cats'] = allCats
    contextDict['addFilter'] = addFilter
    return render( request, "ShowItems.html", contextDict )

def addToCart(request, itemId):
    Prueba.objects.create(texto='add item '+str(itemId))
    return render( request, "popUp.html", {} )
    # return HttpResponse('')

def delFromCart(request, itemId):
    Prueba.objects.create(texto='del item '+str(itemId))
    return render( request, "popUp.html", {} )
    # return HttpResponse('')


