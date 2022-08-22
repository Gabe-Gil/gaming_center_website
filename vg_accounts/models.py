from django.db import models
from django.contrib.auth.models import User
from vg_api.models import Game

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Game, related_name='favorites')

    def __str__(self):
        return f'{self.user.username} Profile'