from django import forms
from .models import Movie, Hall, Session

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'duration', 'genre', 'release_date'] 

class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['name', 'capacity']  

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['movie', 'hall', 'show_time']  # Исправлено на show_time

