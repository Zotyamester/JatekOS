from django.contrib.auth.models import User
from games.models import Game
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        User, verbose_name='Szerző', on_delete=models.CASCADE)
    title = models.CharField('Cím', max_length=300)
    game = models.ForeignKey(
        Game, verbose_name='Játék', on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField('Tartalom')
    pub_date = models.DateTimeField('Közzétételi dátum', default=timezone.now)

    class Meta:
        ordering = ['-pub_date', 'author']

    def __str__(self):
        return self.title + ' - #' + str(self.id)

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    author = models.ForeignKey(
        User, verbose_name='Szerző', on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(
        Post, verbose_name='Poszt', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Tartalom')
    pub_date = models.DateTimeField('Közzétételi dátum', default=timezone.now)

    class Meta:
        ordering = ['-pub_date', 'author']

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'pk': self.post.pk}) + '#comment-' + str(self.pk)
