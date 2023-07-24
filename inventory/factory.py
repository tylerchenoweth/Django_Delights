import factory
from factory.faker import faker

from .models import MenuItem

FAKE = faker.Faker()

class MenuItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MenuItem
    
    title = factory.Faker("sentence", nb_words=2)
    price = factory.Faker("random_number")