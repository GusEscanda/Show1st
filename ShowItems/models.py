from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce import models as tmceModels

from datetime import timedelta
from django.utils import timezone

import uuid

from mainApp.models import Page, SiteSettings
from ShowContact.models import ContactPage

# Create your models here.

class ItemCategory(models.Model):
    name     = models.CharField(max_length=30, unique=True, verbose_name=_('Category'), help_text=_('Create categories and later assign your items to one or many the them.'))
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name=_('Item Category')
        verbose_name_plural=_('Item Categories')
    
    def __str__(self):
        return self.name


class ItemsPage( Page ):

    pageCatFilter = models.ForeignKey(
        ItemCategory, 
        on_delete = models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='pages',
        verbose_name=_('Filter Category'),
        help_text=_('Display only the items that are in the selected category. If none is selected, displays all.')
    )
    headerText = tmceModels.HTMLField( blank=True, null=True, verbose_name=_('Previous text'), help_text=_('Enter text to be displayed before the items grid (optional)'))
    footText = tmceModels.HTMLField( blank=True, null=True, verbose_name=_('Posterior text'), help_text=_('Enter text to be displayed after the items grid (optional)'))
    enableShopCart = models.BooleanField( default=False, verbose_name=_('Enable Shopping Cart'), help_text=_('Allow user to add/remove items to a Shopping Cart and later send you an inquiry email attaching the list.'))
    sendCartPage = models.ForeignKey(
        ContactPage,
        on_delete = models.SET_NULL,
        null=True,
        blank=True,
        related_name='itemPages',
        verbose_name=_('Send Cart Page'),
        help_text=_('Select the Contact Page that will be displayed to allow the user to complete and send the inquiry email.')
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = Page.ITEMS
        self.location = Page.NAVBAR


class Item(models.Model):
    code     = models.CharField(max_length=20, db_index=True, verbose_name=_('Code'), help_text=_('The code that identifies the item'))
    name     = models.CharField(max_length=60, verbose_name=_('Name'), help_text=_('Short name of the item'))
    descrip  = models.TextField(blank=True, verbose_name=_('Description'), help_text=_('Description of the item as you want to appear in the site'))
    thumb    = models.ImageField(upload_to='ShowItems', verbose_name=_('Thumbnail image'), help_text=_('Thumbnail image that will appear in the items grid.'))
    image    = models.ImageField(upload_to='ShowItems', null=True, blank=True, verbose_name=_('Detailed Image'), help_text=_('Large detailed image of the item, designed to cover almost the entire screen'))
    categs   = models.ManyToManyField(ItemCategory, related_name='items', verbose_name=_('Categories'), help_text=_('Select all the categories that this item belongs to.'))
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name=_('Item')
        verbose_name_plural=_('Items')
    
    def strCats(self):
        s = ''
        for cat in self.categs.all():
            s += (', ' if s else '') + cat.name
        return s


    def __str__(self):
        return str(self.code) + ' ' + self.name + '  (' + self.strCats() + ')'


class ShoppingCart( models.Model ):
    cartId  = models.CharField(max_length=100, unique=True, help_text='uuid4 code stored in the session to maintain a separate Shopping Cart for each user browsing the site')
    items   = models.ManyToManyField(Item, help_text='The items list of the Cart')
    updated = models.DateTimeField(auto_now=True, help_text='Last update date, used to automatically clean the unused (abandoned) carts')

    def __str__(self):
        return '{0} ( {1} )'.format(self.cartId, str(self.updated))

    def addItem(self, item):
        self.items.add(item)
        self.updated = timezone.now()
        self.save()

    def delItem(self, item):
        self.items.remove(item)
        self.updated = timezone.now()
        self.save()

    def reset(self):
        self.items.clear()
        self.updated = timezone.now()
        self.save()

    def itemsQty(self):
        return self.items.all().count()

def cleanUnusedCarts(): # delete the expired shopping carts. TODO: consider to call this from a cron job
    expiryTime = SiteSettings.load().cartExpiryTime
    ShoppingCart.objects.filter(updated__lte = timezone.now() - timedelta(days=expiryTime)).delete()

def getCart(session):
    cleanUnusedCarts()
    # Get the current session cart, if there is no cart already create a new one
    if 'cartId' not in session:
        session['cartId'] = str( uuid.uuid4() )
    cart, created = ShoppingCart.objects.get_or_create(cartId=session['cartId'])
    return cart

