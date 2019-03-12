from django.db import models

# Create your models here.


class FoodFitnessModel(models.Model):
    username = models.CharField(max_length=300, default="")
    calories = models.IntegerField()
    date = models.IntegerField()
