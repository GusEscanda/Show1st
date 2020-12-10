from django.db import models
from tinymce import models as tmceModels

from datetime import timedelta
from django.utils import timezone

import uuid

from mainApp.models import Page
from ShowContact.models import ContactPage

# Create your models here.

class ItemCategory(models.Model):
    name     = models.CharField(max_length=30, unique=True, verbose_name='Category')
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Item Category'
        verbose_name_plural='Item Categories'
    
    def __str__(self):
        return self.name


class ItemsPage( Page ):

    pageCatFilter = models.ForeignKey(
        ItemCategory, 
        on_delete = models.CASCADE, 
        null=True, 
        blank=True, 
        verbose_name='Filter Category',
        related_name='pages'
    )
    headerText = tmceModels.HTMLField( blank=True, null=True, verbose_name='Previous text' )
    footText = tmceModels.HTMLField( blank=True, null=True, verbose_name='Posterior text')
    enableShopCart = models.BooleanField( default=False, verbose_name='Enable Shopping Cart')
    sendCartPage = models.ForeignKey(
        ContactPage,
        on_delete = models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Send Cart Page',
        related_name='itemPages'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = Page.ITEMS
        self.location = Page.NAVBAR


class Item(models.Model):
    code     = models.CharField(max_length=20, db_index=True, verbose_name='Code')
    name     = models.CharField(max_length=60, verbose_name='Name')
    descrip  = models.TextField(blank=True, verbose_name='Description')
    thumb    = models.ImageField(upload_to='ShowItems', verbose_name='Small (small)')
    image    = models.ImageField(upload_to='ShowItems', null=True, blank=True, verbose_name='Image (big)')
    categs   = models.ManyToManyField(ItemCategory, verbose_name='Categories', related_name='items')
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Item'
        verbose_name_plural='Items'
    
    def strCats(self):
        s = ''
        for cat in self.categs.all():
            s += (', ' if s else '') + cat.name
        return s


    def __str__(self):
        return str(self.code) + ' ' + self.name + '  (' + self.strCats() + ')'


class ShoppingCart( models.Model ):
    cartId  = models.CharField(max_length=100, unique=True)
    items   = models.ManyToManyField(Item)
    updated = models.DateTimeField(auto_now=True)

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


def getCart(session):
    # delete the expired sessions and shopping carts. TODO: consider to put this in a cron job
    session.clear_expired()
    ShoppingCart.objects.filter(updated__lte = timezone.now() - timedelta(days=15)).delete()
    # if there is no cart already, create a new one
    if 'cartId' not in session:
        session['cartId'] = str( uuid.uuid4() )
    cart, created = ShoppingCart.objects.get_or_create(cartId=session['cartId'])
    return cart

