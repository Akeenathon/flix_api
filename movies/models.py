from django.db import models
from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):
    title = models.CharField(max_length=60)
    release_date = models.DateField(blank=True, null=True)
    resume = models.TextField(max_length=500, blank=True, null=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    genres = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
