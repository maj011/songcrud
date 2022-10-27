from tkinter import CASCADE
from django.db import models


class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_released = models.DateField()
    likes = models.IntegerField()

    def __str__(self):
        return self.title

class Lyric(models.Model):
    the_song_title = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    song_id = models.CharField(max_length=30)

    def __str__(self):
        return self.song_id
