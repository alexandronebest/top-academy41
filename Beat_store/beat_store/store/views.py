from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SongForm, CustomUserCreationForm, ProfileForm
from .models import Song, Genre, Profile
from django.http import HttpResponse

def index(request):
    """
    Главная страница сайта.
    """
    return render(request, 'store/index.html')

@login_required
def profile(request):
    """
    Страница профиля пользователя.
    Отображает информацию о пользователе и его песни.
    """
    profile = get_object_or_404(Profile, user=request.user)
    songs = Song.objects.filter(author=request.user)
    return render(request, 'store/profile.html', {
        'profile': profile,
        'songs': songs
    })

@login_required
def music_list_view(request):
    """
    Страница со списком всех песен.
    Использует select_related для оптимизации запросов к базе данных.
    """
    songs = Song.objects.select_related('author', 'genre').all()
    return render(request, 'store/music_list.html', {'songs': songs})

@login_required
def add_music_view(request):
    """
    Представление для добавления новой песни.
    Обрабатывает как GET, так и POST запросы.
    """
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.author = request.user
            song.save()
            messages.success(request, 'Песня успешно добавлена!')
            return redirect('music_list')
        else:
            messages.error(request, 'Исправьте ошибки в форме')
    else:
        form = SongForm()
    
    return render(request, 'store/add_music.html', {'form': form})

@login_required
def edit_music_view(request, song_id):
    """
    Представление для редактирования существующей песни.
    Проверяет, что автор песни совпадает с текущим пользователем.
    """
    song = get_object_or_404(Song, id=song_id)
    
    if song.author != request.user:
        messages.error(request, 'Вы не можете редактировать эту песню')
        return redirect('music_list')
    
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            messages.success(request, 'Песня успешно обновлена!')
            return redirect('music_list')
    else:
        form = SongForm(instance=song)
    
    return render(request, 'store/edit_music.html', {
        'form': form,
        'song': song
    })

@login_required
def search_view(request):
    """
    Представление для поиска песен по названию.
    """
    query = request.GET.get('query', '').strip()
    results = Song.objects.none()
    
    if query:
        results = Song.objects.filter(title__icontains=query)
    
    return render(request, 'store/search_results.html', {
        'results': results,
        'query': query
    })

def register(request):
    """
    Представление для регистрации нового пользователя.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна!')
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'store/register.html', {'form': form})

@login_required
def upload_song(request):
    """
    Представление для загрузки новой песни.
    """
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            # Здесь можно добавить дополнительную логику, если необходимо
            form.save()
            messages.success(request, 'Песня успешно загружена!')
            return redirect('music_list')
        else:
            messages.error(request, 'Исправьте ошибки в форме')
    else:
        form = SongForm()
    
    return render(request, 'store/upload_song.html', {'form': form})

@login_required
def upload_photo(request):
    profile = request.user.profile  # Предполагается, что у вас есть связанный профиль
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Фото успешно загружено!')
            return redirect('profile')  # Перенаправление на страницу профиля
        else:
            messages.error(request, 'Исправьте ошибки в форме')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'store/upload_photo.html', {'form': form})