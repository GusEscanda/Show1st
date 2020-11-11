from django.contrib import admin

from .models import InfoPage

# Register your models here.

class InfoPageAdmin(admin.ModelAdmin):
    list_display=("position", "app", "location", "name")
    filter_horizontal = ('infLinks',)
    readonly_fields=('app','created','updated')
    ordering = ['position']

admin.site.register(InfoPage, InfoPageAdmin)

