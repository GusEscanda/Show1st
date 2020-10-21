from django.shortcuts import render

from .models import MenuOption

# Create your views here.

def mainPage(request, menuOpt = ''):
    menuContent = MenuOption.objects.filter(optEnabled=True).order_by('optOrder')
    if not menuOpt:
        menuOpt = menuContent[0].optOrder  # asume that the home page is the 1st one in the MenuOption table
    return render( request, "mainPage.html", {'menuOpt':menuOpt, 'menuContent':menuContent} )



