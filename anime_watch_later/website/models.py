from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30, verbose_name='название жанра')

class Entry(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    medium_type = models.CharField(max_length=10, verbose_name='Вид медиа') #тип медиа: фильм сериал аниме книга другое
    #genres = models.ManyToManyField(Genre, verbose_name='жанры', related_name='genre_books')
    priority = models.IntegerField(min_value=0, max_value=3, verbose_name='Приоритет')
    description = models.CharField(max_length=500, verbose_name='Описание')


