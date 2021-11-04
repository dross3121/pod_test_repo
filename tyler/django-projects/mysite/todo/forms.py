from django import forms

class TodoForm(forms.Form):
    task = forms.CharField(label = 'Add a Task', max_length = 255)

class NoteForm(forms.Form):
    note = forms.CharField(label= 'Add a Note', max_length=255)