# -*- coding: utf-8 -*-
# Create your views here.

def subscribe(request):

    form = SubscriptionForm()
    
    context = RequestContext(request, {'form': form})
    
    return render_to_response('subscription/new.html', context)