from django import forms

class AnimeEntryForm(forms.Form):
    name = forms.CharField()    #(max_length=100)
    description = forms.CharField()
