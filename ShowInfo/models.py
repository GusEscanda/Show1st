from django.db import models
from tinymce import models as tmceModels

from mainApp.models import MenuOption

# Create your models here.

class InfoPage(models.Model):
    infCode  = models.SlugField(max_length=20, unique=True, verbose_name='Info Page Code')
    infName  = models.CharField(max_length=40, verbose_name='Info Page Name')
    infText  = tmceModels.HTMLField()
    infLinks = models.ManyToManyField('self', blank=True,  symmetrical=False, verbose_name='Additional Info Links')
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.infCode + ' - ' + self.infName



