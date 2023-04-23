from django.db import models

import datetime

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)

class Ingredient(models.Model):
    
    CUP = "CUP"
    OUNCE = "OZS"
    TABLESPOON = "TBS"
    TEASPOON = "TSP"
    
    UNIT_TYPES = [
        (CUP, "Cup"),
        (OUNCE, "Ounce"),
        (TABLESPOON, "Tablespoon"),
        (TEASPOON, "Teaspoon")
    ]

    name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=3, choices=UNIT_TYPES,)
    unit_price = models.FloatField(default=0.0)

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)

class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    amount_paid = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    