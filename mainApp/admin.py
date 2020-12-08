from django.contrib import admin

from .models import Style, HomePage, SiteSettings

# Register your models here.

class HomePageAdmin(admin.ModelAdmin):
    list_display=("position", "app", "location", "name")
    readonly_fields=('app','location','position','created','updated')
    ordering = ['position']

class StyleAdmin(admin.ModelAdmin):
    list_display=("styleName",)
    readonly_fields=('created','updated')
    ordering = ['styleName']

admin.site.register(SiteSettings)
admin.site.register(Style, StyleAdmin)
admin.site.register(HomePage, HomePageAdmin)


