from django.shortcuts import render

from mainApp.models import MenuOption
from .models import PostTag, Post

# Create your views here.

def showBlog(request, menuOpt, addFilter=''):
    # Obtain the site menu structure
    menuContent = MenuOption.objects.filter( optType = MenuOption.NAVBAR ).order_by('optOrder')
    opt = menuContent.get( optOrder = menuOpt )
    # Init the dictionary to pass to the render
    dictionary = {
        'opt': opt, 
        'menuContent': menuContent, 
        }
    # Obtain the posts, optionally filtered by the opt.optParameter
    filter = opt.optParameter
    if filter:
        filter = [ f.strip() for f in filter.split(',') ] # convert the string into a list
        myPosts = Post.objects.filter( postTags__tagName__in = filter ).order_by('-postDate')
    else:
        myPosts = Post.objects.all().order_by('-postDate')
    # Obtain a list (without duplicates) of ALL the tags that appear in any of the MENU FILTERED posts
    allTags = []
    for post in myPosts:
        for tag in post.postTags.all():
            if tag.tagName not in allTags and tag.tagName not in opt.optParameter :
                allTags.append( tag.tagName )
    # Make the additional filtering
    filter = addFilter
    if filter:
        filter = [ f.strip() for f in filter.split(',') ] # convert the string into a list
        myPosts = myPosts.filter( postTags__tagName__in = filter ).order_by('-postDate')
    # Complete the dictionary
    dictionary['posts'] = myPosts
    dictionary['tags'] = allTags
    dictionary['addFilter'] = addFilter
    return render( request, "ShowBlog.html", dictionary )





