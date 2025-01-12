from django import forms
from .models import Movie, Hall, Session, Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        fields = ['movie', 'hall', 'show_time']  


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['session', 'seats']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']