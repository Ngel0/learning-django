from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Entry
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login

# Create your views here.

def welcome(request):
    return render(request, 'website/welcome.html',
                  {"my_list": Entry.objects.all(),
                  "count_entries": Entry.objects.count()})

def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

# def add(request):
#     if request.method == "POST":
#         form = EntryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = EntryForm()
#     return render(request, 'lists/add.html', {"form": form})

    # submit_button = request.POST.get("submit")
    # anime_name = ''
    # anime_description = ''
    #
    # form = AnimeEntryForm(request.POST or None)
    # if form.is_valid():
    #     anime_name = form.cleaned_data.get("name")
    #     anime_description = form.cleaned_data.get("description")
    #
    # context = {'form': form, 'anime_name': anime_name,
    #            'anime_description': anime_description, 'submit_button': submit_button}
    #
    # return render(request, 'website/welcome.html', context)
