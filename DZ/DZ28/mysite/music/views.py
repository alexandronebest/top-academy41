from django.shortcuts import render
from .models import Music

def music_text(request):
       musics = Music.objects.all()
       return render(request, 'music/music_text.html', {'musics': musics})

def music_text_fr(request):
       musics = Music.objects.all()
       return render(request, 'music/music_text_fr.html', {'musics': musics})

def music_text_de(request):
       musics = Music.objects.all()
       return render(request, 'music/music_text_de.html', {'musics': musics})

def music_text_es(request):
       musics = Music.objects.all()
       return render(request, 'music/music_text_es.html', {'musics': musics})