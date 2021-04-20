from django.db import models
from tinymce import models as tmceModels
from django.utils.translation import gettext_lazy as _

from mainApp.models import Page

# Create your models here.

class ContactPage( Page ):
    enableShopCart = models.BooleanField(
        default = False, 
        verbose_name = _('Enable Shopping Cart'), 
        help_text = _('Display the shopping cart and let the user attach it to an email')
    )
    showSocialMedia = models.BooleanField(
        default = False, 
        verbose_name = _('Show Social Media'), 
        help_text = _('Show the social media of the company')
    )
    text_1 = tmceModels.HTMLField( 
        blank = True, 
        null = True, 
        verbose_name = _('Text 1'), 
        help_text = _('This text will be displayed before the email fields') 
    )
    text_2 = tmceModels.HTMLField( 
        blank = True, 
        null = True, 
        verbose_name = _('Text 2'), 
        help_text = _('This text will be displayed before Shopping Cart related fields') 
    )
    text_3 = tmceModels.HTMLField( 
        blank = True, 
        null = True, 
        verbose_name = _('Text 3'), 
        help_text = _('This text will be displayed at the end of the page, you can put here some not social media contact info, ie: phone number, address, etc.') 
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = Page.CONTACT


class SubjectOption( models.Model ):
    subject = models.CharField(
        max_length = 100, 
        unique = True, 
        verbose_name = _('Subject'), 
        help_text = _("Enter a possible subject for the user's email")
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = _('Mail subject')
        verbose_name_plural = _('Mail subjects')


class MailTo( models.Model ):
    address = models.EmailField( 
        max_length = 100, 
        unique = True, 
        verbose_name = _('Mail Address'),
        help_text = _('Enter an email address in your company, where you want the users be able to send their inquiries')
    )
    
    def __str__(self):
        return self.address

    class Meta:
        verbose_name = _('Mail recipient')
        verbose_name_plural = _('Mail recipients')
    

class SocialMediaOption( models.Model ):
    code = models.CharField(
        max_length = 50, 
        unique = True, 
        verbose_name = _('Social media code'), 
        help_text = _('Code to display the social media icon')
    )

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = _('Social media option')
        verbose_name_plural = _('Social media options')


class SocialMedia( models.Model ):
    order = models.SlugField(
        max_length = 10, 
        unique = True, 
        verbose_name = _('Order'), 
        help_text = _('The social media will be displayed ordered by this field, but this field itself will not be displayed')
    )
    socialMedia = models.ForeignKey(
        SocialMediaOption, 
        on_delete = models.CASCADE, 
        verbose_name = _('Social media'), 
        help_text = _('Select a social media from the list')
    )
    profileName = models.CharField(
        max_length = 50, 
        verbose_name = _('Profile name'), 
        help_text = _("Enter your company's profile name for this social media")
    )
    profileLink = models.URLField(
        verbose_name = _('Profile link'), 
        help_text = _('Enter an URL so the user can click and access directly to your profile')
    )

    def __str__(self):
        return '{} - {} {} - {}'.format(self.order, self.socialMedia.code, self.profileName, self.profileLink)

    class Meta:
        verbose_name = _("Company's social media")
        verbose_name_plural = _("Company's social media")
