# -*- coding: utf-8 -*-
# Create your views here.

from subscription.forms import SubscriptionForm

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def subscribe(request):

    if request.method == 'POST':
        return create(request)
    else:
        return new(request)
        
#    if request.method == 'POST':
#        form = SubscriptionForm(request.POST)
#        if form.is_valid():
#            subscription = form.save()
#            return HttpResponseRedirect(
#            reverse('subscription:success', args=[subscription.pk]))
#        else:
#            form = SubscriptionForm()
    
#    context = RequestContext(request, {'form': form})
    
#    return render_to_response('subscription/new.html', context)

def success(request):

  return render_to_response('subscription/sucesso.html', RequestContext(request))

def new(request):

    form = SubscriptionForm()
    
    context = RequestContext(request, {'form': form})
    
    return render_to_response('subscription/new.html', context)
    
def create(request):

    form = SubscriptionForm(request.POST)
    
    if not form.is_valid():

        context = RequestContext(request, {'form': form})

        return render_to_response('subscription/new.html', context)
        
    subscription = form.save()
    
    return HttpResponseRedirect(reverse('subscription:success', args=[ subscription.pk ]))