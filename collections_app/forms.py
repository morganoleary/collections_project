from django import forms
from .models import CollectorNote
from datetime import date

class CollectorNoteForm(forms.ModelForm):
    class Meta:
        model = CollectorNote
        fields = ['note_title', 'note', 'note_date']
        widgets = {
            'note_date': forms.DateTimeInput(attrs={'value': date.today()}),  # Auto set today's date 
        }
        labels = {
            'note_title': 'Note Title',
            'note': 'Note',
            'note_date': 'Note Date',
        }
