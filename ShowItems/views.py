from django.shortcuts import render

from mainApp.models import MenuOption
from .models import ItemCategory, Item

# Create your views here.

def showItems(request, menuOpt, addFilter=''):
    # Obtain the site menu structure
    menu = MenuOption.objects.all().order_by('optOrder')
    opt = menu.get( optOrder = menuOpt )
    # Init the dictionary to pass to the render
    dictionary = { 'opt': opt, 'menu': menu }
    # Obtain the items, optionally filtered by the opt.optParameter
    filter = opt.optParameter
    if filter:
        filter = [ f.strip() for f in filter.split(',') ] # convert the string into a list
        myItems = Item.objects.filter( itemCats__catName__in = filter ).order_by('itemCode')
    else:
        myItems = Item.objects.all().order_by('itemCode')
    # Obtain a list (without duplicates) of ALL the tags that appear in any of the MENU FILTERED items
    allCats = []
    for item in myItems:
        for cat in item.itemCats.all():
            if cat.catName not in allCats and cat.catName not in opt.optParameter :
                allCats.append( cat.catName )
    # Make the additional filtering
    filter = addFilter
    if filter:
        filter = [ f.strip() for f in filter.split(',') ] # convert the string into a list
        myItems = myItems.filter( itemCats__catName__in = filter ).order_by('itemCode')
    # Complete the dictionary
    dictionary['items'] = myItems
    dictionary['cats'] = allCats
    dictionary['addFilter'] = addFilter
    return render( request, "ShowItems.html", dictionary )





