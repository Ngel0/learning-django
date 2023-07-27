from django.shortcuts import render, redirect, get_object_or_404
from lists.models import Entry
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def welcome(request):
    current_user = request.user
    if current_user.is_authenticated:
        current_entries = Entry.objects.filter(user=current_user.id)
        return render(request, 'website/list.html',
                      {'my_list': current_entries,
                      'count_entries': current_entries.count()})
    else:
        return render(request, 'website/welcome.html')

@login_required
def delete(request, id):
    try:
        entry = Entry.objects.get(pk=id)
        entry.delete()
        return JsonResponse({'success': True})
    except Entry.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Element not found'})
