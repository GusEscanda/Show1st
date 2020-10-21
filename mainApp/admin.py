from django.contrib import admin

from .models import MenuOption

# Register your models here.

class MenuOptionAdmin(admin.ModelAdmin):
    list_display=("optOrder", "optEnabled", "optName", "optType", "optParameter")
    readonly_fields=('created','updated')
    ordering = ['optOrder']


admin.site.register(MenuOption, MenuOptionAdmin)




