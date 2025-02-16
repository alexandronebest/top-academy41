from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Главная страница
    path('profile/', views.profile, name='profile'),  # Страница профиля
    path('music/', views.music_list_view, name='music_list'),  # Список музыки
    path('add_music/', views.add_music_view, name='add_music'),  # Добавление музыки
    path('edit_music/<int:song_id>/', views.edit_music_view, name='edit_music'),  # Редактирование музыки
    path('update_status/', views.update_status, name='update_status'),
]