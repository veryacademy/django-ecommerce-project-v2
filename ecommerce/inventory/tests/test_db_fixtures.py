import pytest
from ecommerce.inventory.models import Category, Product


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name,",
    [
        (1, "widstar running sneakers"),
        (4000, "korkease nain sandals wout box"),
        (8616, "impact puse dance shoe"),
    ],
)
def test_inventory_db_product_dataset(db, django_db_setup, id, name):
    item = Product.objects.get(id=id)
    assert item.name == name


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug",
    [
        (1, "fashion", "fashion"),
        (18, "trainers", "trainers"),
        (36, "baseball", "baseball"),
    ],
)
def test_inventory_db_product_dataset(db, django_db_setup, id, name, slug):
    item = Category.objects.get(id=id)
    assert item.name == name
    assert item.slug == slug


@pytest.mark.parametrize(
    "name, slug",
    [
        ("django", "django"),
        ("book", "book"),
        ("shoe", "shoe"),
    ],
)
def test_cat(db, category_factory, name, slug):
    item = category_factory.create(name=name, slug=slug)
    assert item.name == name
    assert item.slug == slug


@pytest.mark.parametrize("category__name", ["test"])
def test_book(db, category):
    """Instances become fixtures automatically."""
    assert isinstance(category, Category)
    assert category.name == "test"
