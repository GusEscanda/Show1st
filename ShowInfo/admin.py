from django.contrib import admin

from .models import InfoPage

# Register your models here.

class InfoPageAdmin(admin.ModelAdmin):
    list_display = ("infCode","infName")
    filter_horizontal = ('infLinks',)
    readonly_fields = ('created','updated')
    ordering = ['infName']


admin.site.register(InfoPage, InfoPageAdmin)

