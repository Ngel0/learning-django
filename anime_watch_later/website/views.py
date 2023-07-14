from django.shortcuts import render, redirect, get_object_or_404
from lists.models import Entry
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def welcome(request):
    return render(request, 'website/welcome.html',
                  {'my_list': Entry.objects.all(),
                  'count_entries': Entry.objects.count()})

def delete(request, id):
    try:
        entry = Entry.objects.get(pk=id)
        entry.delete()
        return JsonResponse({'success': True})
    except Entry.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Element not found'})
