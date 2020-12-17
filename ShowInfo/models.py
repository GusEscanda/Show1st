from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce import models as tmceModels

from mainApp.models import Page

# Create your models here.

class InfoPage( Page ):

    infText  = tmceModels.HTMLField(verbose_name=_('Text'), help_text=_('Enter the text info to be displayed in this page / menu option'))
    infLinks = models.ManyToManyField('self', blank=True, related_name='linkedBy', verbose_name=_('Additional Info Links'), help_text=_('Select (optional) all the info pages you want to be accessed directly from this one.'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = Page.INFO



