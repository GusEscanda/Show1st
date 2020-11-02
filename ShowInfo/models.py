from django.db import models
from tinymce import models as tmceModels

# Create your models here.

class InfoPage(models.Model):
    infName  = models.SlugField(max_length=20, unique=True, verbose_name='Info Page Name')
    infText  = tmceModels.HTMLField()
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
