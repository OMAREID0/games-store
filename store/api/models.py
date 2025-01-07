from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Category(models.Model):
    name = models.CharField(max_length=200)
    overview = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class GameDetails(models.Model):
    game_name = models.CharField(max_length=200)
    overview = models.CharField(max_length=200)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    banner = models.ImageField()
    screenshots = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.game_name
