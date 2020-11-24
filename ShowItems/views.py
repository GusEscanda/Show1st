from django.shortcuts import render
from django.http import HttpResponse

from mainApp.models import Page
from mainApp.views import getContextDict

from .models import ItemsPage, ItemCategory, Item, ShoppingCart

import uuid     # module that handles unique Ids
from datetime import timedelta
from django.utils import timezone

# Create your views here.


def getCart(session):
    # delete the expired sessions and shopping carts. TODO: consider to put this in a cron job
    session.clear_expired()
    ShoppingCart.objects.filter(updated__lte = timezone.now() - timedelta(days=15)).delete()
    # if there is no cart already, create a new one
    if 'cartId' not in session:
        session['cartId'] = str( uuid.uuid4() )
    cart, created = ShoppingCart.objects.get_or_create(cartId=session['cartId'])
    return cart


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
        cart.items.remove(item)
        cart.updated = timezone.now()
        return HttpResponse('Item removed')
    else:
        cart.items.add(item)
        cart.updated = timezone.now()
        return HttpResponse('Item added')

#    return render( request, "popUp.html", {} )

