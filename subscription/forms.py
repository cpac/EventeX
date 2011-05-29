# -*- coding: utf-8 -*-
# Create your views here.

from django import forms

from subscription.models import Subscription

#class SubscriptionForm(forms.ModelForm) :

#    class Meta:
#        model = Subscription
#        exclude = ('created_at',)

class SubscriptionForm(forms.Form):
        name = forms.CharField()
        cpf = forms.CharField()
        email = forms.EmailField()
        phone = forms.CharField()