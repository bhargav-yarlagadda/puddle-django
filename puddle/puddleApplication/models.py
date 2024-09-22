from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipeName = models.CharField(max_length=50,blank=False)
    recipeDesc = models.TextField()
    recipeImage = models.ImageField(upload_to="recipeImages")
