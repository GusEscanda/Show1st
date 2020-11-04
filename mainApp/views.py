from django.shortcuts import render

from .models import MenuOption, Style

# Create your views here.

def mainPage(request, menuOpt = ''):
    # Obtain the site menu structure
    menuContent = MenuOption.objects.filter( optType = MenuOption.NAVBAR ).order_by('optOrder')
    if menuOpt:
        opt = menuContent.get( optOrder = menuOpt )
    else:
        opt = menuContent[0]  # asume that the home page is the 1st one in the MenuOption table
    # Init the dictionary to pass to the render
    dictionary = {
        'opt': opt, 
        'menuContent': menuContent, 
        }
    return render( request, "mainPage.html", dictionary )


def cssRenderer(request, sName, filename):
    dictionary = {}
    if sName:
        dictionary['style'] = Style.objects.get( styleName = sName )
    return render(request, 'css/' + filename + '.css', dictionary, content_type="text/css")


def jsRenderer(request, filename):
    return render(request, 'js/' + filename + '.js', {}, content_type="text/javascript")

