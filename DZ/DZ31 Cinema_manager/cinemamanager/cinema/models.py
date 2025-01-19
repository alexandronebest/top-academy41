from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название фильма")
    duration = models.PositiveIntegerField(verbose_name="Длительность (мин)")
    genre = models.CharField(max_length=50, verbose_name="Жанр")
    release_date = models.DateField(verbose_name="Дата выхода")

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.title


class Hall(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название зала")
    capacity = models.PositiveIntegerField(verbose_name="Вместимость")

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"

    def __str__(self):
        return self.name


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name="Зал")
    show_time = models.DateTimeField(verbose_name="Время показа")

    class Meta:
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеансы"

    def __str__(self):
        return f"{self.movie.title} в {self.hall.name} во {self.show_time}"
    
    def booked_seats_count(self):
        return Booking.objects.filter(session=self).aggregate(models.Sum('seats'))['seats__sum'] or 0
    


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name="Сеанс")
    seats = models.PositiveIntegerField(verbose_name="Количество мест")
    booking_time = models.DateTimeField(auto_now_add=True, verbose_name="Время бронирования")

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"


    def __str__(self):
        return f"{self.user.username} забронировал {self.seats} мест на {self.session}"


