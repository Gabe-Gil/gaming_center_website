from django.db import models
from vg_api.models import Game
from django.contrib.auth.models import User

# Create your models here.
class Playthrough(models.Model):
    titles = ['temp', 'temp2']

    for i in Game.objects.values_list('title', flat=True):
        titles.append((i, i))
    
    titles.sort()

    game = models.CharField(max_length=2000, choices=titles, default=titles[0])
    playthrough_title = models.CharField(max_length=200, default='Standard')
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'({self.game}) {self.playthrough_title} by {self.owner}'

