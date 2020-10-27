from django.contrib import admin

from .models import ItemCategory, Item

# Register your models here.

class ItemCategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ItemAdmin(admin.ModelAdmin):
    list_display = ("itemCode", "itemName", "categories")
    readonly_fields = ('created','updated')
    ordering = ['itemCode']

    def categories(self, obj):
        return obj.strCats()

admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(Item, ItemAdmin)

