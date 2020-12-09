from django.db import models
from tinymce import models as tmceModels

from mainApp.models import Page

# Create your models here.

class InfoPage( Page ):

    infText  = tmceModels.HTMLField()
    infLinks = models.ManyToManyField('self', blank=True, verbose_name='Additional Info Links', related_name='linkedBy')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = Page.INFO



