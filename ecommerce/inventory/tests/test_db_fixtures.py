import pytest
from django.db import IntegrityError, connection, transaction
from ecommerce.inventory import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (18, "trainers", "trainers", 1),
        (36, "baseball", "baseball", 1),
    ],
)
def test_inventory_db_category_dbfixture(
    db, django_db_setup, id, name, slug, is_active
):
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "name, slug, is_active",
    [
        ("django", "django", 1),
        ("book", "book", 1),
        ("shoe", "shoe", 1),
    ],
)
def test_inventory_db_category_insert_data(
    db, category_factory, name, slug, is_active
):
    result = category_factory.create(name=name, slug=slug, is_active=is_active)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize("category__name", ["test"])
def test_inventory_db_category_insert_data_auto_fixture(db, category):
    """Instances become fixtures automatically."""
    assert isinstance(category, models.Category)
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
    item = models.Product.objects.get(id=id)
    assert item.name == name


# def test_inventory_db_product_insert_data(db, product_factory):

#     test = product_factory.create(category=(1,))

#     item = Product.objects.all().count()
#     item2 = Category.objects.all().count()
#     item3 = Product.objects.get(id=1)
#     item4 = test.category.all()
#     item5 = test.web_id

#     # print(item)
#     # print(item2)
#     # print(item4)
#     # print(item5)


# def test_inventory_db_product_uniqueness_integrity(db, product_factory):
#     web_id = product_factory.create(web_id=123456789)
#     with pytest.raises(IntegrityError):
#         product_factory.create(web_id=123456789)


# def test_inventory_db_producttype_insert_data(db, product_type_factory):

#     type = product_type_factory.create()
#     gettype = ProductType.objects.get(id=1)

#     # print(type.name)
#     # print(gettype.name)


# def test_inventory_db_producttype_uniqueness_integrity(
#     db, product_type_factory
# ):
#     name = product_type_factory.create(name="not_unique")
#     with pytest.raises(IntegrityError):
#         product_type_factory.create(name="not_unique")


# def test_inventory_db_brand_insert_data(db, brand_factory):

#     type = brand_factory.create()
#     gettype = ProductType.objects.get(id=1)

#     # print(type.name)
#     # print(gettype.name)


# def test_inventory_db_brand_uniqueness_integrity(db, brand_factory):
#     name = brand_factory.create(name="not_unique")
#     with pytest.raises(IntegrityError):
#         brand_factory.create(name="not_unique")


# @pytest.mark.dbfixture
# @pytest.mark.parametrize(
#     "id, sku, store_price",
#     [
#         (1, "7633969397", 92.00),
#         (4434, "3012815584", 72.00),
#         (8592, "9789065946", 72.00),
#     ],
# )
# def test_inventory_db_product_inventory_dataset(
#     db, django_db_setup, id, sku, store_price
# ):
#     item = ProductInventory.objects.get(id=id)
#     assert item.sku == sku
#     assert item.store_price == store_price


# def test_inventory_db_product_inventory_insert_data(
#     db, product_inventory_factory
# ):
#     product = product_inventory_factory.create(sku=123456789)
#     assert product.sku == 123456789


# def test_inventory_db_product_inventory_uniqueness_integrity_sku(
#     db, product_inventory_factory
# ):
#     sku = product_inventory_factory.create(sku=1)
#     with pytest.raises(IntegrityError):
#         product_inventory_factory.create(sku=1)


# def test_inventory_db_product_inventory_uniqueness_integrity_upc(
#     db,
#     product_inventory_factory,
# ):

#     with pytest.raises(IntegrityError) as excinfo:
#         new = product_inventory_factory.create(upc=934093051374)
#         connection.check_constraints()

#     assert "UNIQUE constraint failed" in str(excinfo.value)


# @pytest.mark.dbfixture
# @pytest.mark.parametrize(
#     "id, units, units_sold",
#     [
#         (1, 135, 0),
#         (4238, 30, 0),
#         (8616, 100, 0),
#     ],
# )
# def test_inventory_db_stock_dataset(
#     db, django_db_setup, id, units, units_sold
# ):
#     item = Stock.objects.get(id=id)
#     assert item.units == units
#     assert item.units_sold == units_sold


# def test_inventory_db_stock_insert_data(db, stock_factory):
#     product = stock_factory.create()
#     assert product.product_inventory.sku == 7633969398


# @pytest.mark.dbfixture
# @pytest.mark.parametrize(
#     "id, image, alt_text",
#     [
#         (1, "images/default.png", "a default image solid color"),
#     ],
# )
# def test_inventory_db_media_dataset(db, django_db_setup, id, image, alt_text):
#     img = Media.objects.get(id=id)
#     assert img.image == image
#     assert img.alt_text == alt_text


# def test_inventory_db_media_insert_data(db, media_factory):
#     product = media_factory.create()
#     assert product.image == "images/default.png"


# @pytest.mark.dbfixture
# @pytest.mark.parametrize(
#     "id, name, description",
#     [
#         (1, "men-shoe-size", "men shoe size"),
#     ],
# )
# def test_inventory_db_product_attribute_dataset(
#     db, django_db_setup, id, name, description
# ):
#     attr = ProductAttribute.objects.get(id=id)
#     assert attr.name == name
#     assert attr.description == description


# def test_inventory_db_product_attrubite_insert_data(
#     db, product_attribute_factory
# ):
#     attr = product_attribute_factory.create()


# def test_inventory_db_product_attrubite_value_data(
#     db, product_attribute_value_factory
# ):
#     attr = product_attribute_value_factory.create()


# def test_inventory_db_product_attribute_value_data(
#     db, product_with_attribute_values_factory
# ):

#     attr = product_with_attribute_values_factory.create()
#     attr_values = attr.attribute_values.all().count()
#     assert attr_values == 2

#     # t = attr.attribute_values.all()
#     # print(t)
