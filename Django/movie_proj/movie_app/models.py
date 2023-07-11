from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def get_url_directors(self):
        return reverse('director-detail', args=[self.id])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)


    def get_url_actors(self):
        return reverse('actor-detail', args=[self.id])

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.first_name} {self.last_name}'
        else:
            return f'Актриса {self.first_name} {self.last_name}'


# Create your models here.

class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, blank=True, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')
    #slug = models.SlugField(default='', null=True, db_index=True)
    actors = models.ManyToManyField(Actor, related_name='films')

    def get_url(self):
        return reverse('movie-detail', args=[self.id])

    def __str__(self):
        return f'{self.name} - {self.rating}%'

# py manage.py shell_plus --print-sql
# from movie_app.models import Movie
# slug = models.SlugField(default='', null=False, db_index=True)
