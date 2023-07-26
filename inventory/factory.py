import factory
from factory.faker import faker

from .models import MenuItem, Ingredient, RecipeRequirement

FAKE = faker.Faker()


from faker import Faker

fake = Faker()

ingredients_list = [
    'cane sugar','flour', 'egg',
    'milk chocolate', 'butter',
    'orange jelly', 'banilla icing',
    'dough', 'sprinkles'
]

class CustomIngredients(factory.django.DjangoModelFactory):
    class Meta:
        model = Ingredient
    
    fake.sentence(ext_word_list=ingredients_list)

"""class MenuItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MenuItem
    
    title = factory.Faker("sentence", nb_words=2)
    price = factory.Faker("random_number")

class RecipeRequirementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RecipeRequirement
    
    menu_item = #fk 
    ingredient = #fk
    quantity = factory.Faker("random_number")
"""