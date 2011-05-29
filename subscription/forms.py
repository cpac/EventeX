# -*- coding: utf-8 -*-
# Create your views here.

from django import forms
from django.forms.fields import EMPTY_VALUES

from subscription.models import Subscription
from subscription.validators import CpfValidator

from django.utils.translation import ugettext as _
# from subscription import validators

class PhoneWidget(forms.MultiWidget):

    def __init__(self, attrs=None):

        widgets = (
            forms.TextInput(attrs=attrs),
            forms.TextInput(attrs=attrs)
        )

        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):

        if not value:
            return [None, None]
        
        return value.split('-')

class PhoneField(forms.MultiValueField):
    widget = PhoneWidget

    def __init__(self, *args, **kwargs):

        fields = (
            forms.IntegerField(),
            forms.IntegerField()
        )

        super(PhoneField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):

        if not data_list:
            return None

        if data_list[0] in EMPTY_VALUES:
            raise forms.ValidationError(u'DDD inválido.')

        if data_list[1] in EMPTY_VALUES:
            raise forms.ValidationError(u'Número inválido.')

        return '%s-%s' % tuple(data_list)


class SubscriptionForm(forms.ModelForm) :

    phone = PhoneField(label=_('Telefone'), required=False)

    class Meta:
        model = Subscription
        exclude = ('phone','created_at','paid',)

    def clean(self):
        super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise forms.ValidationError(_(u'Informe seu e-mail ou telefone.'))

        return self.cleaned_data

#class SubscriptionForm(forms.Form):
#        name = forms.CharField(label=_('Nome'), max_length=100)
#        cpf = forms.CharField(label=_('CPF'), validators=[CpfValidator])
#        email = forms.EmailField(label=_('E-mail'),required=False)
#        phone = PhoneField(label=_('Telefone'), required=False)
#                #forms.CharField(label=_('Telefone'), required=False,max_length=20)
#
#        def _unique_check(self, fieldname, error_message):
#
#            param = { fieldname: self.cleaned_data[fieldname] }
#
#            try:
#
#                s = Subscription.objects.get(**param)
#
#            except Subscription.DoesNotExist:
#
#                return self.cleaned_data[fieldname]
#
#            raise forms.ValidationError(error_message)
#
#        def clean_cpf(self):
#
#            return self._unique_check('cpf', _(u'CPF já inscrito.'))
#
#        def clean(self):
#
#            if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
#                    raise forms.ValidationError(_(u'Você precisa informar seu e-mail ou seu telefone.'))
#
#            return self.cleaned_data