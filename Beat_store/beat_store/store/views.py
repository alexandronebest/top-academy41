from django.shortcuts import render, redirect
from .models import Song
from django.contrib import messages

def index(request):
    return render(request, 'store/index.html')  # Главная страница

def profile(request):
    return render(request, 'store/profile.html')  # Страница профиля

def music_list_view(request):
    songs = Song.objects.all()
    return render(request, 'store/music_list.html', {'songs': songs})

def add_music_view(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('songTitle')
        if author and title:
            Song.objects.create(author=author, title=title)
            messages.success(request, 'Песня успешно добавлена!')
            return redirect('music_list')
        else:
            messages.error(request, 'Заполните все поля.')
    return render(request, 'store/add_music.html')

def edit_music_view(request, song_id):
    song = Song.objects.get(id=song_id)
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('songTitle')  # Исправлено с request.post на request.POST
        if author and title:
            song.author = author
            song.title = title
            song.save()
            messages.success(request, 'Песня успешно отредактирована!')
        else:
            messages.error(request, 'Заполните все поля.')
        return redirect('music_list')
    return render(request, 'store/edit_music.html', {'song': song})

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