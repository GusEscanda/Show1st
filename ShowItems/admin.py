from django.contrib import admin

from .models import ItemCategory, Item, ItemsPage

# Register your models here.

class ItemsPageAdmin(admin.ModelAdmin):
    list_display=("position", "app", "location", "name")
    readonly_fields=('app','location','created','updated')
    ordering = ['position']

class ItemCategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ItemAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "categories")
    readonly_fields = ('created','updated')
    ordering = ['code']

    def categories(self, obj):
        return obj.strCats()

admin.site.register(ItemsPage, ItemsPageAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(Item, ItemAdmin)

