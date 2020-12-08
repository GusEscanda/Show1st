from django.shortcuts import render
from django.http import HttpResponse

from mainApp.models import Page
from mainApp.views import getContextDict

from .models import ItemsPage, ItemCategory, Item, ShoppingCart, getCart

import uuid     # module that handles unique Ids
from datetime import timedelta
from django.utils import timezone

# Create your views here.

def showItems(request, pageId, addFilter=''):
    context = getContextDict( Page, ItemsPage, pageId )
    # Obtain the items, optionally filtered by pageFilter
    pageFilter = context['page'].pageFilter
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
    context['items'] = myItems
    context['cats'] = allCats
    context['addFilter'] = addFilter
    context['cart'] = getCart(request.session)
    return render( request, "ShowItems.html", context )


def updateCart(request):
    cart = ShoppingCart.objects.get( cartId = request.session['cartId'] )
    item = Item.objects.get( id = request.POST['itemId'] )
    if item in cart.items.all():
        cart.delItem(item)
        return HttpResponse('Item removed')
    else:
        cart.addItem(item)
        return HttpResponse('Item added')

def resetCart(request):
    cart = ShoppingCart.objects.get( cartId = request.session['cartId'] )
    cart.reset()
    return HttpResponse('Item reset')


