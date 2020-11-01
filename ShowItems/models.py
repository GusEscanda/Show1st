from django.db import models

# Create your models here.

from django.db import models
import datetime

# Create your models here.

class ItemCategory(models.Model):
    catName   = models.CharField(max_length=30, unique=True, verbose_name='Category')
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Item Category'
        verbose_name_plural='Item Categories'
    
    def __str__(self):
        return self.catName



class Item(models.Model):
    itemCode     = models.CharField(max_length=20, db_index=True, verbose_name='Code')
    itemName     = models.CharField(max_length=60, verbose_name='Name')
    itemDescrip  = models.TextField(blank=True, verbose_name='Description')
    itemThumb    = models.ImageField(upload_to='ShowItems', verbose_name='Small (small)')
    itemImage    = models.ImageField(upload_to='ShowItems', null=True, blank=True, verbose_name='Image (big)')
    itemCats     = models.ManyToManyField(ItemCategory, verbose_name='Categories')
    created      = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Item'
        verbose_name_plural='Items'
    
    def strCats(self):
        s = ''
        for cat in self.itemCats.all():
            s += (', ' if s else '') + cat.catName
        return s


    def __str__(self):
        return str(self.itemCode) + ' ' + self.itemName + '  (' + self. strCats() + ')'







