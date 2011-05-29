# -*- coding: utf-8 -*-
# Create your views here.

from django import forms

from subscription.models import Subscription
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
        email = forms.EmailField(label=_('E-mail'),required=False)
        phone = forms.CharField(label=_('Telefone'), required=False,max_length=20)

        def _unique_check(self, fieldname, error_message):

            param = { fieldname: self.cleaned_data[fieldname] }

            try:

                s = Subscription.objects.get(**param)

            except Subscription.DoesNotExist:

                return self.cleaned_data[fieldname]

            raise forms.ValidationError(error_message)

        def clean_cpf(self):

            return self._unique_check('cpf', _(u'CPF já inscrito.'))

        def clean(self):

            if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
                    raise forms.ValidationError(_(u'Você precisa informar seu e-mail ou seu telefone.'))

            return self.cleaned_data