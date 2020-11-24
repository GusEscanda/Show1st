from django.db import models
from tinymce import models as tmceModels

from mainApp.models import Page

# Create your models here.

class ContactPage( Page ):
    enableShopCart  = models.BooleanField( default=False, verbose_name='Enable Shopping Cart')
    text_1          = tmceModels.HTMLField( blank=True, null=True, verbose_name='Text 1' )
    text_2          = tmceModels.HTMLField( blank=True, null=True, verbose_name='Text 2' )
    text_3          = tmceModels.HTMLField( blank=True, null=True, verbose_name='Text 3' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = Page.CONTACT
        self.location = Page.NAVBAR

class SubjectOption( models.Model ):
    subject = models.CharField(max_length=100, unique=True, verbose_name='Subject')

    def __str__(self):
        return self.subject


class MailTo( models.Model ):
    address  = models.EmailField(max_length=100, unique=True, verbose_name='Mail Address')
    
    def __str__(self):
        return self.address
    

class ContactChannel( models.Model ):
    order = models.SlugField(max_length=10, unique=True, verbose_name='Order')
    name  = models.CharField(max_length=20, verbose_name='Contact channel')
    icon  = models.ImageField(upload_to='ShowContact', null=True, blank=True, verbose_name='Icon')
    info  = models.CharField(max_length=50, verbose_name='Contact info')

