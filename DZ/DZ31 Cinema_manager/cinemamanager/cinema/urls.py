from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('hall/', views.hall, name='hall'),
    path('sessions/', views.upcoming_sessions, name='upcoming_sessions'),
    path('movies/create/', views.create_movie, name='create_movie'),  # Новый URL
    path('hall/create/', views.create_hall, name='create_hall'),      # Новый URL
    path('sessions/create/', views.create_session, name='create_session'),  # Новый URL
]