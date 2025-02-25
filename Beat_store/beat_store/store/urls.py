from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    

    # Профиль пользователя
    path('profile/', views.profile, name='profile'),

    # Список музыки
    path('music/', views.music_list_view, name='music_list'),

    # Добавление музыки
    path('add-music/', views.add_music_view, name='add_music'),

    # Редактирование музыки
    path('edit-music/<int:song_id>/', views.edit_music_view, name='edit_music'),

    # Загрузка песни
    path('upload-song/', views.upload_song, name='upload-song'),

    # Выход из системы
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

    # Вход в систему
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),

    # Поиск
    path('search/', views.search_view, name='search'),

    # Сброс пароля
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='store/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='store/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='store/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='store/password_reset_complete.html'), name='password_reset_complete'),

    # Регистрация
    path('register/', views.register, name='register'),


    # Загрузка фото
    path('upload-photo/', views.upload_photo, name='upload_photo'),
    #удаление песни
path('delete-music/<int:song_id>/', views.delete_music_view, name='delete_music'),


]