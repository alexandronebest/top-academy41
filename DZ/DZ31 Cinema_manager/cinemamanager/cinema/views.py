from django.shortcuts import render, redirect
from .models import Session, Movie, Hall
from .forms import MovieForm, HallForm, SessionForm

def index(request):
    return render(request, 'cinema/index.html')

def movies(request):
    movies_list = Movie.objects.all()
    return render(request, 'cinema/movies.html', context={'movies': movies_list})

def hall(request):
    hall_list = Hall.objects.all()
    return render(request, 'cinema/hall.html', context={'hall': hall_list})

def upcoming_sessions(request):
    sessions = Session.objects.all()
    return render(request, 'cinema/upcoming_sessions.html', {'sessions': sessions})

def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем фильм
            return redirect('movies')
    else:
        form = MovieForm()
    return render(request, 'cinema/create_movie.html', {'form': form})

def create_hall(request):
    if request.method == 'POST':
        form = HallForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('hall')
    else:
        form = HallForm()
    return render(request, 'cinema/create_hall.html', {'form': form})

def create_session(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('upcoming_sessions')
    else:
        form = SessionForm()
    return render(request, 'cinema/create_session.html', {'form': form})



