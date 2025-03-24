from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.db.models import Count
from .models import User, Song, Genre, Profile
from .forms import SongForm, CustomUserCreationForm, ProfileForm
import logging

logger = logging.getLogger(__name__)

def index(request):
    top_songs = Song.objects.annotate(likes_count=Count('likes')).order_by('-likes_count')[:10]
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
    user = get_object_or_404(User, username=username) if username else request.user
    profile = user.profile
    songs = Song.objects.filter(author=user).select_related('genre')
    liked_songs = user.liked_songs.select_related('author', 'genre').all()

    if request.method == 'POST' and user == request.user:
        profile.status = request.POST.get('status', '').strip()
        profile.save()
        messages.success(request, 'Статус успешно обновлён!')
        return redirect('store:profile', username=user.username)

    context = {
        'profile': profile,
        'songs': songs,
        'liked_songs': liked_songs,
    }
    return render(request, 'store/profile.html', context)

@login_required
def music_list_view(request):
    genres = Genre.objects.all()
    authors = Profile.objects.select_related('user').all()
    songs = Song.objects.select_related('author', 'genre').all()

    if genre_id := request.GET.get('genre'):
        songs = songs.filter(genre__id=genre_id)
    if author_id := request.GET.get('author'):
        songs = songs.filter(author__id=author_id)
    if title := request.GET.get('query'):
        songs = songs.filter(title__icontains=title)

    context = {
        'songs': songs,
        'genres': genres,
        'authors': authors,
    }
    return render(request, 'store/music_list.html', context)

@login_required
def add_music_view(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.author = request.user
            song.save()
            messages.success(request, 'Песня успешно добавлена!')
            return redirect('store:music_list')
        messages.error(request, 'Исправьте ошибки в форме.')
    else:
        form = SongForm()
    return render(request, 'store/add_music.html', {'form': form})

@login_required
def edit_music_view(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if song.author != request.user:
        messages.error(request, 'Вы не можете редактировать эту песню.')
        return redirect('store:music_list')

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            messages.success(request, 'Песня успешно обновлена!')
            return redirect('store:music_list')
        messages.error(request, 'Исправьте ошибки в форме.')
    else:
        form = SongForm(instance=song)
    return render(request, 'store/edit_music.html', {'form': form, 'song': song})

@login_required
def delete_music_view(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if song.author != request.user:
        messages.error(request, 'Вы не можете удалить эту песню.')
        return redirect('store:music_list')

    if request.method == 'POST':
        song.delete()
        messages.success(request, 'Песня успешно удалена!')
        return redirect('store:music_list')
    return render(request, 'store/delete_music.html', {'song': song})

def search_view(request):
    query = request.GET.get('query', '').strip()
    songs = Song.objects.filter(title__icontains=query).select_related('author', 'genre') if query else Song.objects.none()
    return render(request, 'store/search_results.html', {
        'songs': songs,
        'query': query,
    })

class RegisterView(CreateView):
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
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Фото успешно обновлено!')
            return redirect('store:profile', username=request.user.username)
        messages.error(request, 'Исправьте ошибки в форме.')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'store/upload_photo.html', {'form': form})

@login_required
def authors_list_view(request):
    authors = Profile.objects.select_related('user').all()
    return render(request, 'store/profiles.html', {'profiles': authors})

@login_required
@require_POST
@csrf_protect
def like_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    user = request.user
    liked = user in song.likes.all()

    if liked:
        song.likes.remove(user)
        logger.debug(f"User {user.username} unliked song {song_id}")
    else:
        song.likes.add(user)
        logger.debug(f"User {user.username} liked song {song_id}")

    song.save()
    total_likes = song.likes.count()
    return JsonResponse({
        'liked': not liked,
        'total_likes': total_likes,
    }, status=200)

@login_required
@require_POST
@csrf_protect
def play_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    song.total_plays += 1
    song.save()
    logger.debug(f"Song {song_id} played by {request.user.username}, total_plays: {song.total_plays}")
    return JsonResponse({'total_plays': song.total_plays}, status=200)