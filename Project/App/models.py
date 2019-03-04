from django.db import models

# Create your models here.


class FoodFitnessModel(models.Model):
    username = models.CharField(max_length=300, default="")
    calories = models.IntegerField(max_length=10000)
    date = models.IntegerField(max_length=20)
