from django.contrib import admin
from .models import Movie, Hall, Session, Booking

admin.site.site_header = "Управление кинотеатром"
admin.site.site_title = "Админка Cinema Manager"
admin.site.index_title = "Добро пожаловать в Cinema Manager"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'duration')  # Поля для отображения
    list_filter = ('genre', 'release_date')  # Фильтры
    search_fields = ('title', 'genre')  # Поиск по названию и жанру


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')  # Поля для отображения
    search_fields = ('name',)  # Поиск по названию зала


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('movie', 'hall', 'show_time')  # Поля для отображения
    list_filter = ('movie', 'hall', 'show_time')  # Фильтры
    search_fields = ('movie__title', 'hall__name')  # Поиск по названию фильма и зала


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'seats', 'booking_time')  # Поля для отображения
    list_filter = ('session', 'booking_time')  # Фильтры
    search_fields = ('user__username', 'session__movie__title')  # Поиск по пользователю и фильму