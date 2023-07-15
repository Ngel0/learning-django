from django.forms import ModelForm, Textarea, CheckboxSelectMultiple
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'genres': CheckboxSelectMultiple,
            'description': Textarea
        }
