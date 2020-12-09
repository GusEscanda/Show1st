from django.db import models
from django.contrib.auth.models import User
import datetime

from mainApp.models import Page

# Create your models here.

class PostTag(models.Model):
    name     = models.CharField(max_length=30, unique=True, verbose_name='Tag')
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Post Tag'
        verbose_name_plural='Post Tags'
    
    def __str__(self):
        return self.name


class BlogPage( Page ):

    pageFilter = models.ForeignKey( PostTag, 
                                    on_delete=models.CASCADE, 
                                    null=True, 
                                    blank=True, 
                                    verbose_name='Filter Tag',
                                    related_name='pages'
                                   )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = Page.BLOG
        self.location = Page.NAVBAR


class Post(models.Model):
    date     = models.DateField(default=datetime.date.today, db_index=True, verbose_name='Date')
    title    = models.CharField(max_length=60, verbose_name='Title')
    content  = models.TextField(verbose_name='Content')
    image    = models.ImageField(upload_to='ShowBlog', null=True, blank=True, verbose_name='Image')
    author   = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Author', related_name='posts')
    tags     = models.ManyToManyField(PostTag, verbose_name='Tags', related_name='posts')
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
    
    def strTags(self):
        s = ''
        for tag in self.tags.all():
            s += (', ' if s else '') + tag.name
        return s


    def __str__(self):
        return str(self.date) + ' ' + self.title + '  (' + self.strTags() + ')'


