from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from tinymce import models as tmceModels

import datetime

from mainApp.models import Page

# Create your models here.

class PostTag(models.Model):
    name     = models.CharField(max_length=30, unique=True, verbose_name=_('Tag'), help_text=_('Create tags to categorize your posts'))
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name=_('Post Tag')
        verbose_name_plural=_('Post Tags')
    
    def __str__(self):
        return self.name


class BlogPage( Page ):

    DF_ALL       = 0
    DF_TODAY     = 1
    DF_WEEK      = 7
    DF_MONTH     = 30
    DF_TRIMESTER = 90
    DF_YEAR      = 365
    
    DATE_FILTER_CHOICES = [
        (DF_ALL,       'All'),
        (DF_TODAY,     'Today'),
        (DF_WEEK,      'last 7 days'),
        (DF_MONTH,     'last 30 days'),
        (DF_TRIMESTER, 'last 90 days'),
        (DF_YEAR,      'last 365 days'),
    ]

    pageTagFilter = models.ForeignKey(
        PostTag, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='pages',
        verbose_name=_('Filter Tag'),
        help_text=_('Display only the posts with this tag, if not specified display all posts')
    )
    pageDateFilter = models.PositiveIntegerField(
        choices = DATE_FILTER_CHOICES,
        default = DF_ALL, 
        null = False, 
        verbose_name = _('Filter Date'), 
        help_text = _('Filter entries older than x days. 0 means no filtering')
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = Page.BLOG
        self.location = Page.NAVBAR


class Post(models.Model):
    date     = models.DateField(default=datetime.date.today, db_index=True, verbose_name=_('Date'), help_text=_('The date of the post'))
    title    = models.CharField(max_length=60, verbose_name=_('Title'), help_text=_('Title of the post'))
    content  = tmceModels.HTMLField(verbose_name=_('Content'), help_text=_('Enter the content of the post'))
    image    = models.ImageField(upload_to='ShowBlog', null=True, blank=True, verbose_name=_('Image'), help_text=_('Upload a thumbnail image to display with this post'))
    author   = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts', verbose_name=_('Author'), help_text=_('Author of the post'))
    tags     = models.ManyToManyField(PostTag, related_name='posts', verbose_name=_('Tags'), help_text=_('Select all the tags this post is related to.'))
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name=_('Post')
        verbose_name_plural=_('Posts')
    
    def strTags(self):
        s = ''
        for tag in self.tags.all():
            s += (', ' if s else '') + tag.name
        return s


    def __str__(self):
        return str(self.date) + ' ' + self.title + '  (' + self.strTags() + ')'


