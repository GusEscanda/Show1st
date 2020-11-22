from django.db import models

# Create your models here.

class Style(models.Model):
    styleName         = models.SlugField(max_length=20, blank=False, unique=True, verbose_name='Style Name')
    styleBGColor      = models.CharField(max_length=120, blank=True, verbose_name='Background color')
    styleBGImage      = models.ImageField(upload_to='mainApp', null=True, blank=True, verbose_name='Background Image')
    styleTextColor    = models.CharField(max_length=120, blank=True, verbose_name='Text color')
    styleTextBGColor  = models.CharField(max_length=120, blank=True, verbose_name='Text BG color')
    styleInfoBoxColor = models.CharField(max_length=120, blank=True, verbose_name='Info box color')
    created           = models.DateTimeField(auto_now_add=True)
    updated           = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='style'
        verbose_name_plural='styles'
    
    def __str__(self):
        return self.styleName


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
                        verbose_name='Option App'
                    )
    location      = models.CharField( 
                        max_length=6, 
                        choices=[   (NAVBAR, 'NavBar'), 
                                    (FOOTER, 'Footer') ], 
                        blank=True,
                        verbose_name='Location'
                    )
    position      = models.PositiveIntegerField(unique=True, verbose_name='Position')
    homeImage     = models.ImageField(upload_to='mainApp', null=True, blank=True, verbose_name='Home Page Image')
    name          = models.CharField(max_length=30, blank=False, verbose_name='Name')
    mainTitle     = models.CharField(max_length=60, blank=False, verbose_name='Main title')
    imageTitle    = models.ImageField(upload_to='mainApp', null=True, blank=True, verbose_name='Image title')
    style         = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Style')
    created       = models.DateTimeField(auto_now_add=True)
    updated       = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='page'
        verbose_name_plural='pages'
    
    def __str__(self):
        return '{0} - {1} - {2} - {3}'.format(self.position, self.app, self.location, self.name)


class HomePage( Page ):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = Page.HOME
        self.location = Page.NAVBAR
        self.position = 0

