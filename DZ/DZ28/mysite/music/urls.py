from django.urls import path
from . import views

urlpatterns = [
    path('', views.music_text, name='music_text'),
    path('fr/', views.music_text_fr, name='music_text_fr'),
    path('de/', views.music_text_de, name='music_text_de'),
    path('es/', views.music_text_es, name='music_text_es'),
    ]
