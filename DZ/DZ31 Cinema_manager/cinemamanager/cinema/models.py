from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)  # Название
    duration = models.PositiveIntegerField()  # Длительность фильма в минутах
    genre = models.CharField(max_length=50)  # Жанр
    release_date = models.DateField()  # Дата выхода

    def __str__(self):
        return self.title


class Hall(models.Model):
    name = models.CharField(max_length=100)  # Название зала
    capacity = models.PositiveIntegerField()  # Вместимость зала

    def __str__(self):
        return self.name


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Фильм
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)  # Зал
    show_time = models.DateTimeField()  # Время показа

    def __str__(self):
        return f"{self.movie.title} в {self.hall.name} во {self.show_time}"
    
    def booked_seats_count(self):
        return Booking.objects.filter(session=self).aggregate(models.Sum('seats'))['seats__sum'] or 0
    


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, который бронирует билет
    session = models.ForeignKey(Session, on_delete=models.CASCADE)  # Сеанс, на который бронируется билет
    seats = models.PositiveIntegerField()  # Количество забронированных мест
    booking_time = models.DateTimeField(auto_now_add=True)  # Время бронирования

    def __str__(self):
        return f"{self.user.username} забронировал {self.seats} мест на {self.session}"