from django.urls import path
from . import views

app_name = 'store'  # Пространство имен для приложения

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('music/', views.music_list_view, name='music_list'),
    path('add-music/', views.add_music_view, name='add_music'),  # Заменил upload-song
    path('edit-music/<int:song_id>/', views.edit_music_view, name='edit_music'),
    path('delete-music/<int:song_id>/', views.delete_music_view, name='delete_music'),
    path('search/', views.search_view, name='search'),
    path('register/', views.register, name='register'),
    path('upload-photo/', views.upload_photo, name='upload_photo'),
    path('authors/', views.authors_list_view, name='authors_list'),
]