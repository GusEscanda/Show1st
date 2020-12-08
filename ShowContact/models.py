from django.db import models
from tinymce import models as tmceModels

from mainApp.models import Page

# Create your models here.

class ContactPage( Page ):
    enableShopCart  = models.BooleanField( default=False, verbose_name='Enable Shopping Cart')
    showSocialMedia = models.BooleanField( default=False, verbose_name='Show Social Media')
    text_1          = tmceModels.HTMLField( blank=True, null=True, verbose_name='Text 1' )
    text_2          = tmceModels.HTMLField( blank=True, null=True, verbose_name='Text 2' )
    text_3          = tmceModels.HTMLField( blank=True, null=True, verbose_name='Text 3' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = Page.CONTACT


class SubjectOption( models.Model ):
    subject = models.CharField(max_length=100, unique=True, verbose_name='Subject')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name='Mail subject'
        verbose_name_plural='Mail subjects'


class MailTo( models.Model ):
    address  = models.EmailField(max_length=100, unique=True, verbose_name='Mail Address')
    
    def __str__(self):
        return self.address

    class Meta:
        verbose_name='Mail recipient'
        verbose_name_plural='Mail recipients'
    

class SocialMediaOption( models.Model ):
    code = models.CharField(max_length=50, unique=True, verbose_name='Social media code')

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name='Social media option'
        verbose_name_plural='Social media options'


class SocialMedia( models.Model ):
    order       = models.SlugField(max_length=10, unique=True, verbose_name='Order')
    socialMedia = models.ForeignKey(SocialMediaOption, on_delete=models.CASCADE, verbose_name='Social media')
    profileName = models.CharField(max_length=50, verbose_name='Profile name')
    profileLink = models.URLField(verbose_name='Profile link')

    def __str__(self):
        return '{} - {} {} - {}'.format(self.order, self.socialMedia.code, self.profileName, self.profileLink)

    class Meta:
        verbose_name="Company's social media"
        verbose_name_plural="Company's social media"
