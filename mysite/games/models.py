from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Game(models.Model):
    name = models.CharField('Név', max_length=50, unique=True)
    description = models.TextField('Leírás', max_length=500, blank=True)

    def __str__(self):
        return self.name


class Lobby(models.Model):
    owner = models.ForeignKey(
        User, verbose_name='Tulajdonos', on_delete=models.CASCADE, related_name='owned_lobbies')
    name = models.CharField('Név', max_length=50, unique=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('games:lobby-detail', kwargs={'pk': self.pk})


class GameContent(models.Model):
    json = models.JSONField('Json')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
