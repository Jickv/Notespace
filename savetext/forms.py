from django.forms import ModelForm
from savetext.models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['content']