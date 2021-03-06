from django.shortcuts import render_to_response
from django.http import HttpResponse
from nift.models import User

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        user = User.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
            {'books': user, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def search_form(request):
    return render_to_response('search_form.html')

