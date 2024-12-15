from django.db import models

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