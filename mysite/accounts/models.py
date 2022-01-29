from django.contrib.auth.models import User
from django.db import models
from games.models import Lobby
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(
        User, verbose_name='Felhasználó', on_delete=models.CASCADE)
    image = models.ImageField(
        'Profilkép', default='default.png', upload_to='profile_pics')
    bio = models.TextField('Leírás', max_length=500, blank=True)
    playing = models.ForeignKey(Lobby, verbose_name='Aktív játékmenet',
                                on_delete=models.CASCADE, related_name='userprofiles', blank=True, null=True)
    score = models.IntegerField('Pontszám', default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return str(self.user)
