from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template.loader import get_template
from .forms import NoteForm
from django.template import RequestContext

def index(request):
    return render(request, 'index.html', {})

def library(request):
    return render(request, 'library.html', {})

def notezoom(request):
    form = NoteForm(request.POST)
    return render(request, 'notezoom.html', {'form': form})

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note_item = form.save(commit=False)
            note_item.save()
            return render(request, 'notezoom.html', {'form': form})             
        else:
            return render(request, 'notezoom.html', {'form': form})
