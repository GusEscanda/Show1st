from django.shortcuts import render

from mainApp.models import MenuOption
from .models import PostTag, Post

# Create your views here.

def showBlog(request, menuOpt, addFilter=''):
    # Obtain the site menu structure
    menuContent = MenuOption.objects.filter( optEnabled = True ).order_by('optOrder')
    opt = menuContent.get( optOrder = menuOpt )
    # Init the dictionary to pass to the render
    dictionary = {
        'menuOpt': menuOpt, 
        'menuContent': menuContent, 
        'optName': opt.optName, 
        'optParameter': opt.optParameter,
        }
    # Obtain the posts, optionally filtered by the opt.optParameter and the addFilter (additional filter)
    totalFilter = opt.optParameter
    if addFilter:
        totalFilter += (',' if totalFilter else '') + addFilter
    if totalFilter:
        totalFilter = [ f.strip() for f in totalFilter.split(',') ] # convert the string into a list
        posts = Post.objects.filter( postTags__tagName__in = totalFilter ).order_by('postDate')
    else:
        posts = Post.objects.all().order_by('postDate')
    dictionary['posts'] = posts
    # Obtain a list (without duplicates) with ALL the tags that appear in any of the posts to be shown
    tags = []
    for post in posts:
        for tag in post.postTags.all():
            if tag.tagName not in tags:
                tags.append( tag.tagName )
    dictionary['tags'] = tags
    return render( request, "ShowBlog.html", dictionary )





