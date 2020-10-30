from django.contrib import admin

from .models import MenuOption, Style

# Register your models here.

class MenuOptionAdmin(admin.ModelAdmin):
    list_display=("optOrder", "optEnabled", "optName", "optType", "optParameter")
    readonly_fields=('created','updated')
    ordering = ['optOrder']

class StyleAdmin(admin.ModelAdmin):
    list_display=("styleName",)
    readonly_fields=('created','updated')
    ordering = ['styleName']

admin.site.register(MenuOption, MenuOptionAdmin)
admin.site.register(Style, StyleAdmin)




