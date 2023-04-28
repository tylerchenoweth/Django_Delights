from django.contrib import admin

from .models import MenuItem, Ingredient, RecipeRequirement, Purchases

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Ingredient)
admin.site.register(RecipeRequirement)
admin.site.register(Purchases)