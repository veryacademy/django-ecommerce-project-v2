import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from ecommerce.inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = "django"
    slug = "django"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    web_id = 129381723
    slug = "shoe1"
    name = "shoe1"
    description = fake.text()
    is_active = True

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        if extracted:
            # A list of categories were passed in, use them
            for cat in extracted:
                self.category.add(cat)


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductType

    name = fake.lexify(text="type??????")


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand

    name = fake.lexify(text="brand??????")


class ProductInventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductInventory

    sku = 7633969398
    upc = 934093051375
    product_type = factory.SubFactory(ProductTypeFactory)
    product = factory.SubFactory(ProductFactory)
    is_active = 1
    retail_price = 97
    store_price = 92
    sale_price = 46
    weight = 987


register(CategoryFactory)
register(ProductFactory)
register(ProductTypeFactory)
register(BrandFactory)
register(ProductInventoryFactory)
