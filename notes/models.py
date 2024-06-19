from django.db import models  # Import the models module
from django.urls import reverse  # Import reverse

# Note model definition
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# String representation of the model, returns the title
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_detail', args=[str(self.id)])

