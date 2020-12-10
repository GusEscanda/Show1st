from django.contrib import admin
from django import forms

from .models import Style, HomePage, SiteSettings

# Register your models here.

class HomePageAdmin(admin.ModelAdmin):
    list_display=("position", "app", "location", "name")
    readonly_fields=('app','location','position','created','updated')
    ordering = ['position']

class StyleAdmin(admin.ModelAdmin):
    list_display=("name",)
    readonly_fields=('created','updated')
    ordering = ['name']

class SiteSettingsAdminForm(forms.ModelForm):
  class Meta:
    model = SiteSettings
    widgets = {
      'emailHostPassword': forms.PasswordInput(),
    }
    fields = '__all__'

class SiteSettingsAdmin(admin.ModelAdmin):
  form = SiteSettingsAdminForm

admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(HomePage, HomePageAdmin)


