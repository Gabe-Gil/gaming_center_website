from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default=None, blank=True)
    release_date = models.DateField()
    publisher = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    critic_rating = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    user_rating = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    platforms = ArrayField(models.CharField(max_length=20), default=list)
    genres = ArrayField(models.CharField(max_length=20), default=list)
    image_url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='games', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['-created']