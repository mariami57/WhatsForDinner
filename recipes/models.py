from django.db import models

from ingredients.models import Ingredient


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    instructions = models.TextField(max_length=1000)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.title





