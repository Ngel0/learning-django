from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30, verbose_name='название жанра')

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self) -> str:
        return f'{self.name}'

class Entry(models.Model):
    ANIME = 'Аниме'
    SERIES = 'Сериал'
    MOVIE = 'Фильм'
    BOOK = 'Книга'
    OTHER = 'Другое'
    MEDIUM_TYPES = (
        (ANIME, 'Аниме'),
        (SERIES, 'Сериал'),
        (MOVIE, 'Фильм'),
        (BOOK, 'Книга'),
        (OTHER, 'Другое'),
    )
    title = models.CharField(max_length=100, verbose_name='название')
    medium_type = models.CharField(max_length=10, choices=MEDIUM_TYPES, default=ANIME, verbose_name='вид медиа')
    genres = models.ManyToManyField(Genre, verbose_name='жанры', related_name='entries')
    priority = models.IntegerField(default=0, verbose_name='приоритет')
    description = models.CharField(max_length=500, verbose_name='описание')

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'

    def __str__(self) -> str:
        return f'{self.title}'
