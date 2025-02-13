from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Маршрут для главной страницы
    path('profile/', views.profile, name='profile'),  # Маршрут для страницы профиля
]