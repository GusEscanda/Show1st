from django.db import models

from mainApp.models import Page

# Create your models here.

class ContactPage( Page ):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = Page.CONTACT
        self.location = Page.NAVBAR



