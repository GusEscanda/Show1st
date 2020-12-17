from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class SiteSettings( SingletonModel ):
    cartExpiryTime     = models.PositiveIntegerField(default=15, verbose_name='Shopping Carts expiry time (in days)')
    emailHost          = models.CharField(max_length = 100, default = '', blank = True, verbose_name='Email Host')
    emailHostUser      = models.CharField(max_length = 100, default = '', blank = True, verbose_name='Email Host User')
    emailHostPassword  = models.CharField(max_length = 50, default = '', blank = True, verbose_name='Email Host Password')
    emailPort          = models.PositiveIntegerField(default = 587, blank = True, verbose_name='Email Port')
    emailUseTLS        = models.BooleanField(default=True, verbose_name='Email Use TLS')
    emailUseSSL        = models.BooleanField(default=False, verbose_name='Email Use SSL')

    class Meta:
        verbose_name='Site Settings'
        verbose_name_plural='Site Settings'

    def emailConfigured(self):
        return self.emailHost != '' and self.emailHostUser != ''



class Style(models.Model):
    name         = models.SlugField(max_length=20, blank=False, unique=True, verbose_name='Style Name')
    bgColor      = models.CharField(max_length=120, blank=True, verbose_name='Background color')
    bgImage      = models.ImageField(upload_to='mainApp', null=True, blank=True, verbose_name='Background Image')
    textColor    = models.CharField(max_length=120, blank=True, verbose_name='Text color')
    textBGColor  = models.CharField(max_length=120, blank=True, verbose_name='Text BG color')
    infoBoxColor = models.CharField(max_length=120, blank=True, verbose_name='Info box color')
    created      = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='style'
        verbose_name_plural='styles'
    
    def __str__(self):
        return self.name


class Page(models.Model):

    HOME    = 'HOM'
    INFO    = 'INF'
    BLOG    = 'BLG'
    CONTACT = 'CON'
    ITEMS   = 'ITM'

    NAVBAR = 'NAVBAR'
    FOOTER = 'FOOTER'

    app           = models.CharField(
                        max_length=3, 
                        choices=[   (HOME,    'Home'), 
                                    (INFO,    'ShowInfo'), 
                                    (BLOG,    'ShowBlog'), 
                                    (CONTACT, 'ShowContact'),
                                    (ITEMS,   'ShowItems') ], 
                        blank=False,
                        verbose_name=_('Option App'),
                        help_text=_('The App determines the type of information you will show in this menu option of the site')
                    )
    location      = models.CharField(
                        max_length=6, 
                        choices=[   (NAVBAR, 'NavBar'), 
                                    (FOOTER, 'Footer') ], 
                        blank=True,
                        verbose_name=_('Location'),
                        help_text=_('Select where the link to this information will be located: in the nav bar, in the footer or in the body of another page')
                    )
    position      = models.PositiveIntegerField( unique=True, verbose_name=_('Position'),
                                help_text=_('Any numeric value. The menu options / footer links will be displayed ordered by this value, but the value itself will not be displayed.')
                    )
    homeImage     = models.ImageField( upload_to='mainApp', null=True, blank=True, 
                                verbose_name=_('Home Page Image'),
                                help_text=_('Upload an image that will link to this menu option in the home page (optional)')
                    )
    name          = models.CharField( max_length=30, blank=False, verbose_name=_('Name'),
                                help_text=_('The name of this page')
                    )
    mainTitle     = models.CharField( max_length=60, blank=False, verbose_name=_('Main title'),
                                help_text=_('Main title to be displayed at the top of the page')
                    )
    imageTitle    = models.ImageField( upload_to='mainApp', null=True, blank=True, verbose_name=_('Image title'),
                                help_text=_('Load an image if you want to replace the main title with a banner')
                    )
    style         = models.ForeignKey( Style, on_delete=models.SET_NULL, null=True, blank=True, related_name='pages',
                                verbose_name=_('Style'),
                                help_text=_('Select a Style for this menu option or information page')
                    )
    created       = models.DateTimeField(auto_now_add=True)
    updated       = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name=_('page')
        verbose_name_plural=_('pages')
    
    def __str__(self):
        return '{0} - {1} - {2} - {3}'.format(self.position, self.app, self.location, self.name)


class HomePage( Page ):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = Page.HOME
        self.location = Page.NAVBAR
        self.position = 0

