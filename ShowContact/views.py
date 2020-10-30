from django.shortcuts import render

from mainApp.models import MenuOption

# Create your views here.

def showContact(request, menuOpt):
    # Obtain the site menu structure
    menuContent = MenuOption.objects.filter( optEnabled = True ).order_by('optOrder')
    opt = menuContent.get( optOrder = menuOpt )
    # Init the dictionary to pass to the render
    dictionary = {
        'opt': opt, 
        'menuContent': menuContent, 
        }
    return render( request, "ShowContact.html", dictionary )




