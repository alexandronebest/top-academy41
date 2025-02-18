# store/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    path = models.FileField(upload_to='songs/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='songs')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='songs')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.name} {self.user.surname}"