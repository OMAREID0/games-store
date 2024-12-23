from django.db import models

# Create your models here.
class Game_details(models.Model):
    game_name = models.CharField(max_length=200)
    overview = models.CharField(max_length=200)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    price = models.DecimalField(max_digits=3, decimal_places=2)
    banner = models.ImageField()
    screenshots = models.ImageField()


    def __str__(self):
        return self.game_name


class category(models.Model):
    category_name = models.ForeignKey(Game_details, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    overview = models.CharField(max_length=200)