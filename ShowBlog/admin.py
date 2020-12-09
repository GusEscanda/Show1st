from django.contrib import admin

from .models import PostTag, Post, BlogPage

# Register your models here.

class BlogPageAdmin(admin.ModelAdmin):
    list_display=("position", "app", "location", "name")
    readonly_fields=('app','location','created','updated')
    ordering = ['position']

class PostTagAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
    list_display = ("date", "title")
    list_filter = ('date', 'tags__name')
    readonly_fields = ('created','updated')
    ordering = ['-date']

admin.site.register(PostTag, PostTagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(BlogPage, BlogPageAdmin)

