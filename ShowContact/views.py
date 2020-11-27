from django.shortcuts import render
from django.http import HttpResponse
from django.core import mail

from mainApp.models import Page
from mainApp.views import getContextDict

from .models import ContactPage, EmailHostConfig, SocialMedia
from .forms import ContactForm

# Create your views here.

def showContact(request, pageId):
    context = getContextDict( Page, ContactPage, pageId )
    context['smedia'] = SocialMedia.objects.all().order_by('order')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            if not EmailHostConfig.objects.all():
                return HttpResponse('Error: the email Host is not configured...')
            conf = EmailHostConfig.objects.get(configId=1)
            cd = form.cleaned_data
            email = mail.EmailMessage()
            email.subject    = cd['subject'].subject
            email.body       = cd['message']
            email.from_email = cd['sender']
            email.reply_to   = [ cd['sender'] ]
            email.to         = [ cd['mailTo'].address ]
            if cd['ccMyself']:
                email.cc = [ cd['sender'] ]
            if cd['attachSC']:
                pass # TODO: makde the CSV attachment based on the shopping cart and attach it to the email
            with mail.get_connection(
                fail_silently = False,             # TODO: after the debugging process make fail_silently=True
                host          = conf.emailHost, 
                port          = conf.emailPort, 
                username      = conf.emailHostUser, 
                password      = conf.emailHostPassword, 
                use_tls       = conf.emailUseTLS, 
                use_ssl       = conf.emailUseSSL
            ) as connection:
                email.connection = connection
                email.send()
            # clear the form data and allow to start a new process
            form = ContactForm()
        # if the form is not valid, leave it unchanged so the templete will display the errors
    else: # if method != 'POST' (it's the 1st call to the form page) create an empty form and present it to the user
        form = ContactForm()
    context['form'] = form
    return render( request, "ShowContact.html", context )

