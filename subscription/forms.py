# -*- coding: utf-8 -*-
# Create your views here.

from django import forms

#from subscription.models import Subscription
from subscription.validators import CpfValidator

from django.utils.translation import ugettext as _
from subscription import validators

#class SubscriptionForm(forms.ModelForm) :

#    class Meta:
#        model = Subscription
#        exclude = ('created_at',)

class SubscriptionForm(forms.Form):
        name = forms.CharField(label=_('Nome'), max_length=100)
        cpf = forms.CharField(label=_('CPF'), validators=[CpfValidator])
        email = forms.EmailField(label=_('E-mail'))
        phone = forms.CharField(label=_('Telefone'), required=False,max_length=20)