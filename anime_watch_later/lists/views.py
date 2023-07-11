from django.shortcuts import render, redirect
from .forms import EntryForm

# Create your views here.
def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EntryForm()
    return render(request, 'lists/add.html', {'form': form})
