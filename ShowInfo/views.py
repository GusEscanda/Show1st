from django.shortcuts import render

from mainApp.models import MenuOption

from .models import InfoPage

# Create your views here.

def showInfo(request, menuOpt):
    # Obtain the site menu structure
    menuContent = MenuOption.objects.filter( optEnabled = True ).order_by('optOrder')
    opt = menuContent.get( optOrder = menuOpt )
    # Init the dictionary to pass to the render
    dictionary = {
        'opt': opt, 
        'menuContent': menuContent, 
        }
    inf = InfoPage.objects.get(infName = opt.optParameter)
    dictionary['inf'] = inf
    return render( request, "ShowInfo.html", dictionary )




