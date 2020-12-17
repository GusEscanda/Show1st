from django import forms
from django.utils.translation import gettext_lazy as _


from .models import SubjectOption, MailTo
from ShowItems.models import ShoppingCart, Item

class ContactForm(forms.Form):
    sender      = forms.EmailField(label=_('Your email address'))
    ccMyself    = forms.BooleanField(label=_('Cc yourself'), initial=True, required=False, help_text=_('Check to receive a copy of this email'))
    mailTo      = forms.ModelChoiceField(label=_('Send mail to'), 
                                queryset=MailTo.objects.all(),
                                to_field_name='address',
                                help_text=_('Select a recipient')
                )
    subject     = forms.ModelChoiceField(label=_('Subject'), 
                                queryset=SubjectOption.objects.all(),
                                to_field_name='subject',
                                help_text=_('Select a subject from the list')
                )
    message     = forms.CharField(label=_('Message'), widget=forms.Textarea)
    attachSC    = forms.BooleanField(label=_('Attach Shopping Cart'), initial=True, required=False, help_text=_('Check to attach a copy of the Shopping Cart to your mail'))
    clearSC     = forms.BooleanField(label=_('Clear after send'), initial=True, required=False, help_text=_('Clear the Shopping Cart after send it'))

class ItemsCartForm(forms.Form):
    code     = forms.CharField( max_length=20, widget=forms.TextInput(attrs={'readonly': True}) )
    name     = forms.CharField( max_length=60, widget=forms.TextInput(attrs={'readonly': True}) )
    quantity = forms.IntegerField( min_value=0 )

