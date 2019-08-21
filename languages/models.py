from django.db import models

# Create your models here.
class Paradigm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length = 50)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length = 50)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length = 100)

    def __str(self):
        return self.name


class Movies(models.Model):
    movie_name = models.CharField(max_length = 150)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.movie_name
