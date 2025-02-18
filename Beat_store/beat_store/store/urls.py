from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('music/', views.music_list_view, name='music_list'),
    path('add-music/', views.add_music_view, name='add-music'),  # Используем дефис
    path('edit-music/<int:song_id>/', views.edit_music_view, name='edit-music'),
    path('update-status/', views.update_status, name='update-status'),
    path('upload-song/', views.upload_song, name='upload-song'),
]