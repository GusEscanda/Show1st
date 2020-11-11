from django.contrib import admin

from .models import ContactPage

# Register your models here.

class ContactPageAdmin(admin.ModelAdmin):
    list_display=("position", "app", "location", "name")
    readonly_fields=('app','location','created','updated')
    ordering = ['position']

admin.site.register(ContactPage, ContactPageAdmin)

