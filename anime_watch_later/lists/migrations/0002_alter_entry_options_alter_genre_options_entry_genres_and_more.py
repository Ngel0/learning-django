# Generated by Django 4.2.2 on 2023-07-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': 'запись', 'verbose_name_plural': 'записи'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'жанр', 'verbose_name_plural': 'жанры'},
        ),
        migrations.AddField(
            model_name='entry',
            name='genres',
            field=models.ManyToManyField(related_name='entries', to='lists.genre', verbose_name='жанры'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.CharField(max_length=500, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='medium_type',
            field=models.CharField(choices=[('anime', 'Аниме'), ('series', 'Сериал'), ('movie', 'Фильм'), ('book', 'Книга'), ('other', 'Другое')], default='anime', max_length=10, verbose_name='вид медиа'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='priority',
            field=models.IntegerField(default=0, verbose_name='приоритет'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
    ]
