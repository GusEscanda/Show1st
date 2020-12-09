from django.shortcuts import render

from mainApp.models import Page
from mainApp.views import getContextDict

from .models import BlogPage, PostTag, Post

# Create your views here.

def showBlog(request, pageId, addFilter=''):
    contextDict = getContextDict( Page, BlogPage, pageId )
    # Obtain the items, optionally filtered by pageFilter
    pageFilter = contextDict['page'].pageFilter
    if pageFilter:
        myPosts = pageFilter.posts.all().order_by('-date')
        tagFiltered = pageFilter.name
    else:
        myPosts = Post.objects.all().order_by('-date')
        tagFiltered = ''
    # Obtain a list (without duplicates) of ALL the tags that appear in any of the MENU FILTERED posts
    allTags = []
    for post in myPosts:
        for tag in post.tags.all():
            if tag.name not in allTags and tag.name != tagFiltered:
                allTags.append( tag.name )
    # Make the additional filtering
    filter = addFilter
    if filter:
        filter = [ f.strip() for f in filter.split(',') ] # convert the string into a list
        myPosts = myPosts.filter( tags__name__in = filter ).order_by('-date')
    # Complete the context dictionary
    contextDict['posts'] = myPosts
    contextDict['tags'] = allTags
    contextDict['addFilter'] = addFilter
    return render( request, "ShowBlog.html", contextDict )





