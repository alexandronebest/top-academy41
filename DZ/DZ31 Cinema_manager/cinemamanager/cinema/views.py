from django.shortcuts import render, redirect, get_object_or_404
from .models import Session, Movie, Hall, Booking
from .forms import MovieForm, HallForm, SessionForm, BookingForm



def index(request):
    return render(request, 'cinema/index.html')

def movies(request):
    movies_list = Movie.objects.all()
    return render(request, 'cinema/movies.html', context={'movies': movies_list})

def hall(request):
    hall_list = Hall.objects.all()
    return render(request, 'cinema/hall.html', context={'hall': hall_list})

def upcoming_sessions(request):
    sessions = Session.objects.all().prefetch_related('booking_set')
    for session in sessions:
        session.booked_seats = session.booked_seats_count()
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

def change_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'cinema/change_movie.html', {'form': form})

def change_session(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('upcoming_sessions')
    else:
        form = SessionForm(instance=session)
    return render(request, 'cinema/change_session.html', {'form': form})

def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies')
    return render(request, 'cinema/delete_movie.html', {'movie': movie})

def create_booking(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  # Создаем объект бронирования, но не сохраняем в БД
            booking.user = request.user  # Присваиваем текущего пользователя
            booking.save()  # Сохраняем бронирование
            return redirect('upcoming_sessions')  # Перенаправление на страницу с сеансами
    else:
        form = BookingForm(initial={'session': session})  # Инициализируем форму с текущим сеансом

    return render(request, 'cinema/create_booking.html', {'form': form, 'session': session})

