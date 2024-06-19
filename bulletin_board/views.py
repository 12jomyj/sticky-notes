
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from notes.models import Note
from django.shortcuts import render

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'

class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('main_menu')  # Redirect to the main menu after creating a note

class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('main_menu')  # Redirect to the main menu after updating a note

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('main_menu')  # Redirect to the main menu after deleting a note

# Add a simple main menu view
def main_menu_view(request):
    return render(request, 'notes/main_menu.html')