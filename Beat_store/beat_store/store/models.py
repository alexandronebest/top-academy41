from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Электронная почта')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Song(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    path = models.FileField(upload_to='songs/', verbose_name='Файл')
    cover = models.ImageField(upload_to='covers/', null=True, blank=True, verbose_name='Обложка')
    likes = models.ManyToManyField(
        User,
        related_name='liked_songs',
        blank=True,
        verbose_name='Лайки'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='songs',
        verbose_name='Автор'
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Жанр'
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00,
        verbose_name='Цена'
    )
    total_plays = models.PositiveIntegerField(default=0, verbose_name='Количество прослушиваний', db_index=True)  # Добавлен индекс
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
        ordering = ['-created_at']


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Пользователь'
    )
    status = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name='Статус'
    )
    photo = models.ImageField(
        upload_to='profile_photos/',
        null=True,
        blank=True,
        verbose_name='Фото'
    )

    def __str__(self):
        return f'Профиль {self.user.username}'

    @property
    def total_likes(self):
        """Сумма лайков всех песен пользователя."""
        return sum(song.total_likes for song in self.user.songs.all())

    @property
    def total_plays(self):
        """Сумма прослушиваний всех песен пользователя."""
        return sum(song.total_plays for song in self.user.songs.all())

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()