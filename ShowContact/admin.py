from django.contrib import admin

from .models import ContactPage, SubjectOption, MailTo, SocialMediaOption, SocialMedia

# Register your models here.

class ContactPageAdmin(admin.ModelAdmin):
    list_display=("position", "app", "location", "name")
    readonly_fields=('app','created','updated')
    ordering = ['position']

class EmailHostConfigAdmin(admin.ModelAdmin):
    list_display=("emailHost","emailHostUser", "emailPort")
    readonly_fields=('configId',)

class SubjectOptionAdmin(admin.ModelAdmin):
    list_display=("subject",)
    ordering = ['subject']

class MailToAdmin(admin.ModelAdmin):
    list_display=('address',)
    ordering = ['address']

class SocialMediaOptionAdmin(admin.ModelAdmin):
    list_display=('code',)
    ordering = ['code']

class SocialMediaAdmin(admin.ModelAdmin):
    list_display=('order', 'socialMedia', 'profileName', 'profileLink')
    ordering = ['order']

admin.site.register(ContactPage, ContactPageAdmin)
admin.site.register(SubjectOption, SubjectOptionAdmin)
admin.site.register(MailTo, MailToAdmin)
admin.site.register(SocialMediaOption, SocialMediaOptionAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
