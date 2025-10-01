from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipes',  blank=True, null=True)
    instructions = models.TextField(max_length=1000)
    ingredients = models.TextField(max_length=1000)
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()

    @property
    def total_time(self):
        return self.prep_time + self.cook_time


    def __str__(self):
        return self.title





