from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    instructions = models.TextField(max_length=1000)