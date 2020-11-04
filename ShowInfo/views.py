from django.shortcuts import render

from mainApp.models import MenuOption

from .models import InfoPage

# Create your views here.

def showInfo(request, menuOpt, infoPage=''):
    # Obtain the site menu structure
    menu = MenuOption.objects.all().order_by('optOrder')
    opt = menu.get( optOrder = menuOpt )
    # Init the dictionary to pass to the render
    dictionary = { 'opt': opt, 'menu': menu }
    inf = InfoPage.objects.get(infCode = (infoPage if infoPage else opt.optParameter) )
    dictionary['inf'] = inf
    return render( request, "ShowInfo.html", dictionary )




