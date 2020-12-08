from django import forms

from .models import SubjectOption, MailTo
from ShowItems.models import ShoppingCart, Item

class ContactForm(forms.Form):
    sender      = forms.EmailField(label='Your email address')
    ccMyself    = forms.BooleanField(label='Cc yourself', initial=True, required=False)
    mailTo      = forms.ModelChoiceField(label='Send mail to', 
                                queryset=MailTo.objects.all(),
                                to_field_name='address'
                )
    subject     = forms.ModelChoiceField(label='Subject', 
                                queryset=SubjectOption.objects.all(),
                                to_field_name='subject'
                )
    message     = forms.CharField(label='Message', widget=forms.Textarea)
    attachSC    = forms.BooleanField(label='Attach Shopping Cart', initial=True, required=False)
    clearSC     = forms.BooleanField(label='Clear Shopping Cart after send it', initial=True, required=False)

class ItemsCartForm(forms.Form):
    code     = forms.CharField( max_length=20, widget=forms.TextInput(attrs={'readonly': True}) )
    name     = forms.CharField( max_length=60, widget=forms.TextInput(attrs={'readonly': True}) )
    quantity = forms.IntegerField( min_value=0 )

