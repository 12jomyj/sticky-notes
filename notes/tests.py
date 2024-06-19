# notes/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteTests(TestCase):
    
    def setUp(self):
        self.note = Note.objects.create(title='Test Note', content='This is a test note.')

    def test_create_note_view(self):
        response = self.client.get(reverse('note_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_form.html')

        response = self.client.post(reverse('note_create'), {'title': 'New Note', 'content': 'This is a new note.'})
        self.assertEqual(response.status_code, 302)  # Redirects after creating a note
        self.assertEqual(Note.objects.count(), 2)
        self.assertRedirects(response, reverse('main_menu'))

    def test_edit_note_view(self):
        response = self.client.get(reverse('note_edit', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_form.html')

        response = self.client.post(reverse('note_edit', args=[self.note.id]), {'title': 'Updated Note', 'content': 'This is an updated note.'})
        self.assertEqual(response.status_code, 302)  # Redirects after updating a note
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')
        self.assertRedirects(response, reverse('main_menu'))

    def test_delete_note_view(self):
        response = self.client.post(reverse('note_delete', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after deleting a note
        self.assertEqual(Note.objects.count(), 0)
        self.assertRedirects(response, reverse('main_menu'))