from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30, verbose_name='название жанра')
    def __str__(self) -> str:
        return f'{self.name}'

class Entry(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    medium_type = models.CharField(max_length=10, verbose_name='Вид медиа') #тип медиа: фильм сериал аниме книга другое
    #genres = models.ManyToManyField(Genre, verbose_name='жанры', related_name='genre_books')
    #fgsdg = models.CharField(max_length=10) #добавив поле я не могу добраться до уже существующих
    priority = models.IntegerField(default=0, verbose_name='Приоритет')
    description = models.CharField(max_length=500, verbose_name='Описание')

    def __str__(self) -> str:
        return f'{self.title}'
