from django.db import models
from django.core.urlresolvers import reverse


class Recipe(models.Model):
    name        = models.CharField(max_length=200)
    ingredients = models.TextField(help_text='Separate each item by comma')
    details     = models.TextField()
    image       = models.ImageField( 
        null=True, 
        blank=True, 
        width_field="width_field", 
        height_field="height_field"
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'id': self.id})

    def get_ingredients(self):
        return self.ingredients.split(',')
