from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template.loader import get_template
from savetext.forms import NoteForm
from savetext.models import Note
from django.template import RequestContext

def index(request):
    return render(request, 'index.html', {})

def library(request):
    return render(request, 'library.html', {})

def notezoom(request):
        form = NoteForm(request.POST) 
        if request.method == 'POST':

            form = NoteForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'notezoom.html', {'form': form})            
        else:
            form = NoteForm(request.POST)

            return render(request, 'notezoom.html', {'form': form})
