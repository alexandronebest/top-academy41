from django.shortcuts import render, redirect
from .models import Song, Genre
from django.contrib import messages
from .forms import SongForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'store/index.html')  # Главная страница

@login_required
def profile(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        if hasattr(request.user, 'profile'):
            request.user.profile.status = status
            request.user.profile.save()
            messages.success(request, 'Статус успешно обновлен!')
        else:
            messages.error(request, 'Профиль не найден.')
        return redirect('profile')
    return render(request, 'store/profile.html')

@login_required
def music_list_view(request):
    songs = Song.objects.all()
    return render(request, 'store/music_list.html', {'songs': songs})

@login_required
def add_music_view(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.author = request.user
            song.save()
            messages.success(request, 'Песня успешно добавлена!')
            return redirect('music_list')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = SongForm()
    return render(request, 'store/add_music.html', {'form': form})

@login_required
def edit_music_view(request, song_id):
    song = Song.objects.get(id=song_id)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            song = form.save()
            messages.success(request, 'Песня успешно отредактирована!')
            return redirect('music_list')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = SongForm(instance=song)
    return render(request, 'store/edit_music.html', {'form': form, 'song': song})

@login_required
def update_status(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        if status:
            request.user.profile.status = status
            request.user.profile.save()
            messages.success(request, 'Статус успешно обновлен!')
        else:
            messages.error(request, 'Статус не может быть пустым.')
    return redirect('profile')

@login_required
def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.author = request.user
            song.save()
            messages.success(request, 'Песня успешно загружена!')
            return redirect('music_list')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = SongForm()
    return render(request, 'store/upload_song.html', {'form': form})

def search_view(request):
    query = request.GET.get('query', '')
    if query:
        # Простой поиск по названию песни
        results = Song.objects.filter(title__icontains=query)
    else:
        results = Song.objects.none()
    return render(request, 'store/search_results.html', {'results': results, 'query': query})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправляем на страницу входа после успешной регистрации
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})