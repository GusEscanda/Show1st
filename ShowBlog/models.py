from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class PostTag(models.Model):
    tagName   = models.CharField(max_length=30, unique=True, verbose_name='Tag')
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Post Tag'
        verbose_name_plural='Post Tags'
    
    def __str__(self):
        return self.tagName



class Post(models.Model):
    postDate     = models.DateField(default=datetime.date.today, db_index=True, verbose_name='Date')
    postTitle    = models.CharField(max_length=50, verbose_name='Title')
    postContent  = models.CharField(max_length=500, verbose_name='Content')
    postImage    = models.ImageField(upload_to='ShowBlog', null=True, blank=True, verbose_name='Image')
    postAuthor   = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Author')
    postTags     = models.ManyToManyField(PostTag, verbose_name='Tags')
    created      = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
    
    def strTags(self):
        s = ''
        for tag in self.postTags.all():
            s += (', ' if s else '') + tag.tagName
        return s


    def __str__(self):
        return str(self.postDate) + ' ' + self.postTitle + '  (' + self.strTags() + ')'







