# myapp/management/commands/populatedb.py

from django.core.management.base import BaseCommand
from inventory.models import Ingredient, MenuItem, RecipeRequirement, Purchases

class Command(BaseCommand):
    help = 'Populate the database with initial data.'

    def handle(self, *args, **kwargs):
        # Create and save instances of YourModel
        i1 = Ingredient.objects.create(name='Milk Chocolate', quantity='56', unit='OZS', unit_price='.63')
        i2 = Ingredient.objects.create(name='Flour', quantity='56', unit='OZS', unit_price='.06')
        i3 = Ingredient.objects.create(name='Cane Sugar', quantity='56', unit='OZS', unit_price='.8')
        i4 = Ingredient.objects.create(name='Egg', quantity='56', unit='LRG', unit_price='.5')
        i5 = Ingredient.objects.create(name='Orange Jelly', quantity='56', unit='GRM', unit_price='.03')
        
        m1 = MenuItem.objects.create(title="Django Djaffa Cake", price="8.25")

        i1.save()
        i2.save()
        i3.save()
        i4.save()
        i5.save()

        m1.save()

        RecipeRequirement.objects.create(menu_item=m1, ingredient=i1, quantity='6')
        RecipeRequirement.objects.create(menu_item=m1, ingredient=i2, quantity='1')
        RecipeRequirement.objects.create(menu_item=m1, ingredient=i3, quantity='1.5')
        RecipeRequirement.objects.create(menu_item=m1, ingredient=i4, quantity='1')
        RecipeRequirement.objects.create(menu_item=m1, ingredient=i5, quantity='100')

        Purchases.objects.create(menu_item=m1, amount_paid=m1.price, timestamp='2023-04-27 22:45:38')

        self.stdout.write(self.style.SUCCESS('Database great success!'))