from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import mail
from django import forms

from mainApp.models import Page, SiteSettings
from mainApp.views import getContextDict

from ShowItems.models import ShoppingCart, getCart

from .models import ContactPage, SocialMedia
from .forms import ContactForm, ItemsCartForm

import csv, io

# Create your views here.

def createCSV(data, fieldnames):
    csvfile = io.StringIO()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
    return csvfile.getvalue()


def showContact(request, pageId, returnPageApp='', returnPageId=0):
    context = getContextDict( Page, ContactPage, pageId )
    settings = SiteSettings.load()
    context['settings'] = settings
    context['smedia'] = SocialMedia.objects.all().order_by('order')
    ItemsCartFormSet = forms.formset_factory( ItemsCartForm, extra = 0 )
    cart = getCart(request.session)
    cartData = []
    for item in cart.items.all():
        cartData.append( {
            'code': item.itemCode,
            'name': item.itemName,
            'quantity': 0
        } )
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm( request.POST, prefix='contact' )
        formset = ItemsCartFormSet( request.POST, request.FILES, initial=cartData, prefix='cart' )
        # check whether it's valid:
        formValid = form.is_valid()       # not putting the functions directly in the 'if' statement because
        formsetValid = formset.is_valid() # the 'and' makes the 2nd one not evaluate if the 1st fails
        if formValid and formsetValid:
            # process the data in form.cleaned_data as required
            if not settings.emailConfigured():
                return HttpResponse('Error: the email Host is not configured...')
            cd = form.cleaned_data
            email = mail.EmailMessage()
            email.subject    = cd['subject'].subject
            email.body       = cd['message']
            email.from_email = cd['sender']
            email.reply_to   = [ cd['sender'] ]
            email.to         = [ cd['mailTo'].address ]
            if cd['ccMyself']:
                email.cc = [ cd['sender'] ]
            if cd['attachSC'] and context['page'].enableShopCart:
                itemsCSV = createCSV(formset.cleaned_data, ['code', 'name', 'quantity'])
                email.attach('items.csv', itemsCSV, 'text/csv')
                if cd['clearSC']:
                    cart.reset()
            with mail.get_connection(
                fail_silently = False,             # TODO: after the debugging process make fail_silently=True
                host          = settings.emailHost, 
                port          = settings.emailPort, 
                username      = settings.emailHostUser, 
                password      = settings.emailHostPassword, 
                use_tls       = settings.emailUseTLS, 
                use_ssl       = settings.emailUseSSL
            ) as connection:
                email.connection = connection
                email.send()
            # clear the form data and allow to start a new process
            if returnPageId:
                redir = '/{}/{}'.format(returnPageApp,returnPageId)
            else:
                redir = request.path
            return HttpResponseRedirect(redir)
        else:
            pass # if the form is not valid, leave it unchanged so the templete will display the errors
    else: # if method != 'POST' (it's the 1st call to the form page) create an empty form and present it to the user
        form = ContactForm( prefix='contact' )
        formset = ItemsCartFormSet( initial=cartData, prefix='cart' )
    context['form'] = form
    context['formset'] = formset
    return render( request, "ShowContact.html", context )

