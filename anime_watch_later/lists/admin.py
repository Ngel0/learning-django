from django.contrib import admin

from .models import Genre, Entry
# Register your models here.
admin.site.register(Genre)
admin.site.register(Entry)
