from django.db import models

# Create your models here.
class Recipe(models.Model):
    item_name = models.CharField(max_length= 100)
    ingredients = models.CharField(max_length= 200)
    process = models.CharField(max_length=300)

    def __str__(self):
        template = '{0.item_name} {0.ingredients} {0.process}'
        return template.format(self)

