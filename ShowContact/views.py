from django.shortcuts import render

from mainApp.models import MenuOption

# Create your views here.

def showContact(request, menuOpt):
    # Obtain the site menu structure
    menu = MenuOption.objects.all().order_by('optOrder')
    opt = menu.get( optOrder = menuOpt )
    # Init the dictionary to pass to the render
    dictionary = { 'opt': opt, 'menu': menu }
    return render( request, "ShowContact.html", dictionary )




