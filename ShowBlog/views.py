from django.shortcuts import render

from django.utils import timezone
from datetime import timedelta

from mainApp.models import Page
from mainApp.views import getContextDict

from .models import BlogPage, PostTag, Post

# Create your views here.

def showBlog(request, pageId, addTagFilter='', addDateFilter=0):
    context = getContextDict( Page, BlogPage, pageId )
    # Obtain the items, optionally filtered by pageTagFilter and pageDateFiltert
    pageTagFilter = context['page'].pageTagFilter
    if pageTagFilter:
        myPosts = pageTagFilter.posts.all().order_by('-date')
        tagFiltered = pageTagFilter.name
    else:
        myPosts = Post.objects.all().order_by('-date')
        tagFiltered = ''
    pageDateFilter = context['page'].pageDateFilter
    if pageDateFilter:
        myPosts = myPosts.filter( date__gt = timezone.now()-timedelta(days=pageDateFilter) ).order_by('-date')
    # Obtain a list (without duplicates) of ALL the tags that appear in any of the MENU FILTERED posts
    allTags = []
    for post in myPosts:
        for tag in post.tags.all():
            if tag.name not in allTags and tag.name != tagFiltered:
                allTags.append( tag.name )
    # Make the additional filtering (addTagFilter and addDateFilter)
    filter = addTagFilter
    if filter:
        filter = [ f.strip() for f in filter.split(',') ] # convert the string into a list
        myPosts = myPosts.filter( tags__name__in = filter ).order_by('-date')
    if addDateFilter:
        myPosts = myPosts.filter( date__gt = timezone.now()-timedelta(days=addDateFilter) ).order_by('-date')
    # Complete the context dictionary
    context['posts'] = myPosts
    context['tags'] = allTags
    context['addTagFilter'] = addTagFilter
    context['addDateFilter'] = addDateFilter
    return render( request, "ShowBlog.html", context )





