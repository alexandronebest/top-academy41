from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('hall/', views.hall, name='hall'),
    path('sessions/', views.upcoming_sessions, name='upcoming_sessions'),
    path('movies/create/', views.create_movie, name='create_movie'),  
    path('hall/create/', views.create_hall, name='create_hall'),      
    path('sessions/create/', views.create_session, name='create_session'),
    path('change_movie/<int:movie_id>/', views.change_movie, name='change_movie'),
    path('change_session/<int:session_id>/', views.change_session, name='change_session'),
    path('delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('sessions/<int:session_id>/book/', views.create_booking, name='create_booking'),
    
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
      
]