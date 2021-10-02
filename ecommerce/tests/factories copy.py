import factory
from ecommerce.inventory import models
from faker import Faker
from pytest_factoryboy import register

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = "django"
    slug = "django"


register(CategoryFactory)
