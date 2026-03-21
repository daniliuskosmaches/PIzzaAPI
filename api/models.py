from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
#Entity
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
#Entity
class Chef(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, related_name='chef')
#Entity
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
#Entity
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    cheese_type = models.CharField(max_length=50)
    dough_thickness = models.CharField(max_length=20)
    secret_ingredient = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='pizzas')
    ingredients = models.ManyToManyField(Ingredient, related_name='pizzas')
#Entity
class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField(
        #that is needed to validate that the rating is integer and in range 1-5
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )


# Create your models here.





