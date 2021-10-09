import pytest
from django.db import IntegrityError, connection, transaction
from ecommerce.inventory.models import (
    Category,
    Product,
    ProductInventory,
    ProductType,
)


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug",
    [
        (1, "fashion", "fashion"),
        (18, "trainers", "trainers"),
        (36, "baseball", "baseball"),
    ],
)
def test_inventory_db_category_dataset(db, django_db_setup, id, name, slug):
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
def test_inventory_db_category_insert_data(db, category_factory, name, slug):
    item = category_factory.create(name=name, slug=slug)
    assert item.name == name
    assert item.slug == slug


@pytest.mark.parametrize("category__name", ["test"])
def test_inventory_db_category_insert_data_auto_fixture(db, category):
    """Instances become fixtures automatically."""
    assert isinstance(category, Category)
    assert category.name == "test"


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


def test_inventory_db_product_insert_data(db, product_factory):

    test = product_factory.create(category=(1,))

    item = Product.objects.all().count()
    item2 = Category.objects.all().count()
    item3 = Product.objects.get(id=1)
    item4 = test.category.all()
    item5 = test.web_id

    print(item)
    print(item2)
    print(item4)
    print(item5)


def test_inventory_db_product_uniqueness_integrity(db, product_factory):
    web_id = product_factory.create(web_id=123456789)
    with pytest.raises(IntegrityError):
        product_factory.create(web_id=123456789)


def test_inventory_db_producttype_insert_data(db, product_type_factory):

    type = product_type_factory.create()
    gettype = ProductType.objects.get(id=1)

    print(type.name)
    print(gettype.name)


def test_inventory_db_producttype_uniqueness_integrity(
    db, product_type_factory
):
    name = product_type_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        product_type_factory.create(name="not_unique")


def test_inventory_db_brand_insert_data(db, brand_factory):

    type = brand_factory.create()
    gettype = ProductType.objects.get(id=1)

    print(type.name)
    print(gettype.name)


def test_inventory_db_brand_uniqueness_integrity(db, brand_factory):
    name = brand_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        brand_factory.create(name="not_unique")


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, sku, store_price",
    [
        (1, "7633969397", 92.00),
        (4434, "3012815584", 72.00),
        (8592, "9789065946", 72.00),
    ],
)
def test_inventory_db_product_inventory_dataset(
    db, django_db_setup, id, sku, store_price
):
    item = ProductInventory.objects.get(id=id)
    assert item.sku == sku
    assert item.store_price == store_price


def test_inventory_db_product_inventory_insert_data(
    db, product_inventory_factory
):
    product = product_inventory_factory.create(sku=123456789)
    assert product.sku == 123456789


def test_inventory_db_product_inventory_uniqueness_integrity_sku(
    db, product_inventory_factory
):
    sku = product_inventory_factory.create(sku=1)
    with pytest.raises(IntegrityError):
        product_inventory_factory.create(sku=1)


def test_inventory_db_product_inventory_uniqueness_integrity_upc(
    db,
    product_inventory_factory,
):

    with pytest.raises(IntegrityError) as excinfo:
        new = product_inventory_factory.create(upc=934093051374)
        connection.check_constraints()

    assert "UNIQUE constraint failed" in str(excinfo.value)
