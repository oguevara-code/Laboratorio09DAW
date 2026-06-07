from django.db import models

# Create your models here.


# Uno a muchos (One To Many)

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
class Framework(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
    

# Muchos a muchos (Many To Many)

class Movie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class Character(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name