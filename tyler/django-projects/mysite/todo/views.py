from django.shortcuts import render
from .models import Todo, Note
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NoteForm, TodoForm

# Create your views here.
def todo(request):
    if request.method == 'GET':
        # tasks is our queryset of Todo objects
        tasks = Todo.objects.all()
        # instance of the todo form class
        form = TodoForm()
        return render(request = request,
                      template_name= 'list.html',
                      context = {'tasks':tasks,
                                 'form': form})

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            # add new Todo obeject to Queryset
            Todo.objects.create(task=task)
        return HttpResponseRedirect(reverse('todo'))

def task(request, task_id, completed = False):
    if request.method == 'GET':
        # looking up specific todo object by primary key
        todo = Todo.objects.get(pk=task_id)
        # make a form, repopulate character field with the name of the task
        form = TodoForm(initial={'task': todo.task})
        return render(request = request,
                      template_name= 'detail.html',
                      context = {
                          'form':form,
                          'task_id':task_id,
                      })
    if request.method == 'POST':
        if 'save' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task=form.cleaned_data['task']
                #update task attribute of the task of the correct task_id 
                Todo.objects.filter(pk=task_id).update(task=task)
        elif 'complete' in request.POST:
            Todo.objects.filter(pk=task_id).update(completed = True)
            

        elif 'delete' in request.POST:
            Todo.objects.filter(pk=task_id).delete()
        return HttpResponseRedirect(reverse('todo'))

def note(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        form = NoteForm()
        return render(request = request,
                      template_name= 'notes.html',
                      context= { 'form': form,
                                 'notes': notes
                                })

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note_text=form.cleaned_data['note']
            Note.objects.create(note_text=note_text)
        return HttpResponseRedirect(reverse('note'))
