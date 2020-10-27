from django.shortcuts import render

from .models import MenuOption

# Create your views here.

def mainPage(request, menuOpt = ''):
    menuContent = MenuOption.objects.filter(optEnabled=True).order_by('optOrder')
    if not menuOpt:
        menuOpt = menuContent[0].optOrder  # asume that the home page is the 1st one in the MenuOption table
    return render( request, "mainPage.html", {'menuOpt':menuOpt, 'menuContent':menuContent} )


def cssRenderer(request, filename):
    dictionary = {'colorInfoBlock': 'linear-gradient( 325deg, rgba(2,0,36,1) 0%, rgba(9,121,86,1) 0%, rgba(0,212,255,1) 100%)'}
    return render(request, 'css/' + filename + '.css', dictionary, content_type="text/css")


def jsRenderer(request, filename):
    return render(request, 'js/' + filename + '.js', {}, content_type="text/javascript")

