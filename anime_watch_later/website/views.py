from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Entry
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def welcome(request):
    return render(request, 'website/welcome.html',
                  {'my_list': Entry.objects.all(),
                  'count_entries': Entry.objects.count()})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            new_user = authenticate(username=username, password=form.cleaned_data['password1'])
            messages.success(request, f'Аккаунт успешно создан для пользователся {username}.')
            login(request, new_user)
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})
