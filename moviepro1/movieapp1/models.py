from django.db import models

from django.db import models

class TeluguData(models.Model):
    movie_name = models.CharField(max_length=60)
    director_name = models.CharField(max_length=40)
    hero_name = models.CharField(max_length=20)
    heroine_name = models.CharField(max_length=20)
    producer_name = models.CharField(max_length=30)
    release_date = models.DateField()
class EnglishData(models.Model):
    movie_name = models.CharField(max_length=60)
    director_name = models.CharField(max_length=40)
    hero_name = models.CharField(max_length=20)
    heroine_name = models.CharField(max_length=20)
    producer_name = models.CharField(max_length=30)
    release_date = models.DateField()
class HindiData(models.Model):
    movie_name = models.CharField(max_length=60)
    director_name = models.CharField(max_length=40)
    hero_name = models.CharField(max_length=20)
    heroine_name = models.CharField(max_length=20)
    producer_name = models.CharField(max_length=30)
    release_date = models.DateField()
class UserData(models.Model):
    movie_name = models.CharField(max_length=60)
    director_name = models.CharField(max_length=40)
    hero_name = models.CharField(max_length=20)
    heroine_name = models.CharField(max_length=20)
    producer_name = models.CharField(max_length=30)
    release_date = models.DateField()


