# -*- coding: utf-8 -*-
# Create your views here.

from django import forms

#from subscription.models import Subscription

from django.utils.translation import ugettext as _

#class SubscriptionForm(forms.ModelForm) :

#    class Meta:
#        model = Subscription
#        exclude = ('created_at',)

class SubscriptionForm(forms.Form):
        name = forms.CharField(label=_('Nome'), max_length=100)
        cpf = forms.CharField(label=_('CPF'), max_length=11,min_length=11)
        email = forms.EmailField(label=_('E-mail'))
        phone = forms.CharField(label=_('Telefone'), required=False,max_length=20)