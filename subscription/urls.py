# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from route import route

urlpatterns = patterns('subscription.views',

        #url(r'^$', 'subscribe', name='subscribe'),
        route(r'^$',GET='new',POST='create',name='subscribe'),
        url(r'^(?P<id_inscricao>\d+)/sucesso/$', 'success', name='success'),
)
