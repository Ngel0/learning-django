from django.shortcuts import render
from django.http import HttpResponse
from .forms import AnimeEntryForm


# Create your views here.

def welcome(request):
    submit_button = request.POST.get("submit")
    anime_name = ''
    anime_description = ''

    form = AnimeEntryForm(request.POST or None)
    if form.is_valid():
        anime_name = form.cleaned_data.get("name")
        anime_description = form.cleaned_data.get("description")

    context = {'form': form, 'anime_name': anime_name,
               'anime_description': anime_description, 'submit_button': submit_button}

    return render(request, 'website/welcome.html', context)
