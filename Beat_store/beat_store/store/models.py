from django.db import models

class Song(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.author} - {self.title}"