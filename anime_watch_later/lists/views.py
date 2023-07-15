from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add(request):
    if request.method == 'POST':
        instance = Entry(user=request.user)
        form = EntryForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EntryForm()
    return render(request, 'lists/add.html', {'form': form})
