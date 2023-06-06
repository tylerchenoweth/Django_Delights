from django.db import models

import datetime

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=50, unique=True)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    
    CUP = "CUP"
    OUNCE = "OZS"
    TABLESPOON = "TBS"
    TEASPOON = "TSP"
    GRAM = "GRM"
    BOX = "BOX"
    SMALL = "SML"
    MEDIUM = "MED"
    LARGE = "LRG"
    POUND = "LBS"

    UNIT_TYPES = [
        (CUP, "Cup"),
        (OUNCE, "Ounce"),
        (TABLESPOON, "Tablespoon"),
        (TEASPOON, "Teaspoon"),
        (BOX, "Box"),
        (GRAM,"Gram"),
        (LARGE,"Large"),
        (MEDIUM,"Medium"),
        (SMALL,"Small"),
        (POUND, "LBS"),
    ]

    name = models.CharField(max_length=30, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=3, choices=UNIT_TYPES)
    unit_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)

    def __str__(self):
        return self.menu_item.title + " - " + self.ingredient.name

class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    amount_paid = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.menu_item.title
         