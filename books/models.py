from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    cover = models.ImageField(
        upload_to='images/', default='images/default.png')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
