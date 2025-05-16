from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1, 'Avaliação deve ser maior ou igual a 1'),
            MaxValueValidator(5, 'Avaliação deve ser menor ou igual a 5'),
        ]
    )
    comment = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.movie
