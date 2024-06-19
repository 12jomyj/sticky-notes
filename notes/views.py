# notes/views.py

from django.shortcuts import render  # Import render
from django.urls import reverse_lazy  # Import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note
from .forms import NoteForm

# Existing class-based views...

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')

def main_menu_view(request):
    return render(request, 'notes/main_menu.html')
