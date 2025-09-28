from django.db import models



# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipes',  blank=True, null=True)
    instructions = models.TextField(max_length=1000)
    ingredients = models.TextField(max_length=1000)

    def __str__(self):
        return self.title





