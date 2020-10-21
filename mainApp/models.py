from django.db import models

# Create your models here.

class MenuOption(models.Model):
    HOME    = 'HOM'
    INFO    = 'INF'
    BLOG    = 'BLG'
    CONTACT = 'CON'
    ITEMS   = 'ITM'

    optOrder     = models.CharField(max_length=10, unique=True, verbose_name='Order')
    optEnabled   = models.BooleanField(default=True, verbose_name='Enabled')
    optName      = models.CharField(max_length=30, blank=False, verbose_name='Option Name')
    optType      = models.CharField( 
                     max_length=3, 
                     choices=[ (HOME,    'Home'), 
                               (INFO,    'ShowInfo'), 
                               (BLOG,    'ShowBlog'), 
                               (CONTACT, 'ShowContact'),
                               (ITEMS,   'ShowItems') ], 
                     default=INFO,
                     verbose_name='Option Type'
                   )
    optParameter = models.CharField(max_length=60, blank=True, verbose_name='Aditional Parameter')
    created      = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)
    
    class Meta: # buscar en la documentacion oficial de django 'model meta options' para ver opciones adicionales para poner en los modelos (ej: verbose_name)
        verbose_name='menu option'
        verbose_name_plural='menu options'
    
    def __str__(self):
        return self.optOrder + ' ' + self.optName + ( ' - ' + self.optParameter if self.optParameter else '' )



