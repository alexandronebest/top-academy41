from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from .models import User, Song, Genre, Profile
from .forms import SongForm, CustomUserCreationForm, ProfileForm

def index(request):
    """Отображает главную страницу с топом песен, новинками, жанрами и авторами."""
    top_songs = Song.objects.order_by('-created_at')[:10]
    new_songs = Song.objects.order_by('-created_at')[:10]
    genres = Genre.objects.all()
    authors = Profile.objects.select_related('user').all()

    context = {
        'top_songs': top_songs,
        'new_songs': new_songs,
        'genres': genres,
        'authors': authors,
    }
    return render(request, 'store/index.html', context)

@login_required
def profile(request, username=None):
    """Отображает профиль пользователя и позволяет редактировать статус."""
    user = get_object_or_404(User, username=username) if username else request.user
    profile = get_object_or_404(Profile, user=user)
    songs = Song.objects.filter(author=user).select_related('genre')
    liked_songs = user.liked_songs.all()

    if request.method == 'POST' and user == request.user:
        profile.status = request.POST.get('status', '')
        profile.save()
        messages.success(request, 'Статус обновлен!')
        return redirect('store:profile', username=user.username)

    context = {
        'profile': profile,
        'songs': songs,
        'liked_songs': liked_songs,
        'viewed_user': user,
        'is_own_profile': user == request.user
    }
    return render(request, 'store/profile.html', context)

@login_required
def music_list_view(request):
    """Отображает список песен с фильтрацией по жанру, автору и названию."""
    genres = Genre.objects.all()
    authors = Profile.objects.select_related('user').all()
    songs = Song.objects.select_related('author', 'genre').all()

    genre_id = request.GET.get('genre')
    if genre_id:
        songs = songs.filter(genre__id=genre_id)
    author_id = request.GET.get('author')
    if author_id:
        songs = songs.filter(author__id=author_id)
    title = request.GET.get('query')
    if title:
        songs = songs.filter(title__icontains=title)

    context = {
        'songs': songs,
        'genres': genres,
        'authors': authors,
    }
    return render(request, 'store/music_list.html', context)

@login_required
def add_music_view(request):
    """Позволяет пользователю добавить новую песню."""
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.author = request.user
            song.save()
            messages.success(request, 'Песня успешно добавлена!')
            return redirect('store:music_list')
        messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = SongForm()
    return render(request, 'store/add_music.html', {'form': form})

@login_required
def edit_music_view(request, song_id):
    """Позволяет автору редактировать свою песню."""
    song = get_object_or_404(Song, id=song_id)
    if song.author != request.user:
        messages.error(request, 'Вы не можете редактировать эту песню')
        return redirect('store:music_list')

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            messages.success(request, 'Песня успешно обновлена!')
            return redirect('store:music_list')
    else:
        form = SongForm(instance=song)
    return render(request, 'store/edit_music.html', {'form': form, 'song': song})

@login_required
def delete_music_view(request, song_id):
    """Позволяет автору удалить свою песню."""
    song = get_object_or_404(Song, id=song_id)
    if song.author != request.user:
        messages.error(request, 'Вы не можете удалить эту песню')
        return redirect('store:music_list')

    if request.method == 'POST':
        song.delete()
        messages.success(request, 'Песня успешно удалена!')
        return redirect('store:music_list')
    return render(request, 'store/delete_music.html', {'song': song})

def search_view(request):
    """Поиск песен по названию."""
    query = request.GET.get('query', '').strip()
    results = Song.objects.filter(title__icontains=query) if query else Song.objects.none()
    return render(request, 'store/search_results.html', {
        'results': results,
        'query': query
    })

class RegisterView(CreateView):
    """Регистрация нового пользователя."""
    form_class = CustomUserCreationForm
    template_name = 'store/register.html'
    success_url = reverse_lazy('store:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Регистрация прошла успешно!')
        return super().form_valid(form)

@login_required
def upload_photo(request):
    """Обновление фото профиля пользователя."""
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Фото успешно обновлено!')
            return redirect('store:profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'store/upload_photo.html', {'form': form})

@login_required
def authors_list_view(request):
    """Отображает список всех авторов."""
    authors = Profile.objects.select_related('user').all()
    return render(request, 'store/profiles.html', {'profiles': authors})

@login_required
@require_POST  # Ограничиваем метод только POST
@csrf_protect  # Явно включаем защиту CSRF
def like_song(request, song_id):
    """Обработка лайка/дизлайка песни через AJAX."""
    song = get_object_or_404(Song, id=song_id)
    user = request.user

    # Проверяем, лайкнул ли пользователь песню ранее
    if user in song.likes.all():
        song.likes.remove(user)
        liked = False
    else:
        song.likes.add(user)
        liked = True

    # Сохраняем изменения и возвращаем JSON-ответ
    song.save()
    return JsonResponse({
        'liked': liked,
        'total_likes': song.total_likes,  # Используем свойство модели
    }, status=200)
