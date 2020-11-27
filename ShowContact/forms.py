from django import forms

from .models import SubjectOption, MailTo

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

    