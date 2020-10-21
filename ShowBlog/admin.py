from django.contrib import admin

from .models import PostTag, Post

# Register your models here.

class PostTagAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
    list_display = ("postDate", "postTitle", "tags")
    readonly_fields = ('created','updated')
    ordering = ['-postDate']

    def tags(self, obj):
        return obj.strTags()

admin.site.register(PostTag, PostTagAdmin)
admin.site.register(Post, PostAdmin)







