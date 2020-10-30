from django.db import models

# Create your models here.

class Style(models.Model):
    styleName         = models.CharField(max_length=20, blank=False, unique=True, verbose_name='Style Name')
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



class MenuOption(models.Model):
    HOME    = 'HOM'
    INFO    = 'INF'
    BLOG    = 'BLG'
    CONTACT = 'CON'
    ITEMS   = 'ITM'

    optOrder      = models.CharField(max_length=10, unique=True, verbose_name='Order')
    optEnabled    = models.BooleanField(default=True, verbose_name='Enabled')
    optName       = models.CharField(max_length=30, blank=False, verbose_name='Option Name')
    optType       = models.CharField( 
                      max_length=3, 
                      choices=[ (HOME,    'Home'), 
                                (INFO,    'ShowInfo'), 
                                (BLOG,    'ShowBlog'), 
                                (CONTACT, 'ShowContact'),
                                (ITEMS,   'ShowItems') ], 
                      default=INFO,
                      verbose_name='Option Type'
                    )
    optParameter  = models.CharField(max_length=60, blank=True, verbose_name='Aditional Parameter')
    optStyle      = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Style')
    optMainTitle  = models.CharField(max_length=60, blank=False, verbose_name='Main title')
    optImageTitle = models.ImageField(upload_to='mainApp', null=True, blank=True, verbose_name='Image title')
    created       = models.DateTimeField(auto_now_add=True)
    updated       = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='menu option'
        verbose_name_plural='menu options'
    
    def __str__(self):
        return self.optOrder + ' ' + self.optName + ( ' - ' + self.optParameter if self.optParameter else '' )



