from django.shortcuts import render

from mainApp.models import MenuOption

# Create your views here.

def showContact(request, menuOpt):
    menuContent = list( MenuOption.objects.filter(optEnabled=True).order_by('optOrder') )
    return render( request, "ShowContact.html", {'menuOpt':menuOpt, 'menuContent':menuContent} )




