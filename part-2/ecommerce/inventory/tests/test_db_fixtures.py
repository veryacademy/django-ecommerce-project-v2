import pytest
from django.db import IntegrityError
from ecommerce.inventory import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (18, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),
    ],
)
def test_inventory_category_dbfixture(
    db, db_fixture_setup, id, name, slug, is_active
):
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "slug, is_active",
    [
        ("fashion", 1),
        ("trainers", 1),
        ("baseball", 1),
    ],
)
def test_inventory_db_category_insert_data(
    db, category_factory, slug, is_active
):
    result = category_factory.create(slug=slug, is_active=is_active)
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, web_id, name, slug, description, is_active, created_at, updated_at",
    [
        (
            1,
            "45425810",
            "widstar running sneakers",
            "widstar-running-sneakers",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            8616,
            "45434425",
            "impact puse dance shoe",
            "impact-puse-dance-shoe",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_db_product_dbfixture(
    db,
    django_db_setup,
    id,
    web_id,
    name,
    slug,
    description,
    is_active,
    created_at,
    updated_at,
):
    result = models.Product.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.web_id == web_id
    assert result.name == name
    assert result.slug == slug
    assert result.description == description
    assert result.is_active == is_active
    assert result_created_at == created_at
    assert result_updated_at == updated_at


def test_inventory_db_product_uniqueness_integrity(db, product_factory):
    new_web_id = product_factory.create(web_id=123456789)
    with pytest.raises(IntegrityError):
        product_factory.create(web_id=123456789)


@pytest.mark.dbfixture
def test_inventory_db_product_insert_data(
    db, product_factory, category_factory
):

    new_product = product_factory.create(category=(1, 2, 3, 4, 5))
    result_product_category = new_product.category.all().count()
    assert "web_id_" in new_product.web_id
    assert result_product_category == 5


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, sku, upc, product_type, product, brand, is_active, retail_price, store_price, sale_price, weight, created_at, updated_at",
    [
        (
            1,
            "7633969397",
            "934093051374",
            1,
            1,
            1,
            1,
            97.00,
            92.00,
            46.00,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            8616,
            "3880741573",
            "844935525855",
            1,
            8616,
            1253,
            1,
            89.00,
            84.00,
            42.00,
            929,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_db_product_inventory_dataset(
    db,
    db_fixture_setup,
    id,
    sku,
    upc,
    product_type,
    product,
    brand,
    is_active,
    retail_price,
    store_price,
    sale_price,
    weight,
    created_at,
    updated_at,
):
    result = models.ProductInventory.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.sku == sku
    assert result.upc == upc
    assert result.product_type.id == product_type
    assert result.product.id == product
    assert result.brand.id == brand
    assert result.is_active == is_active
    assert result.retail_price == retail_price
    assert result.store_price == store_price
    assert result.sale_price == sale_price
    assert result.weight == weight
    assert result_created_at == created_at
    assert result_updated_at == updated_at


def test_inventory_db_product_inventory_insert_data(
    db, product_inventory_factory
):
    new_product = product_inventory_factory.create(
        sku="123456789",
        upc="123456789",
        product_type__name="new_name",
        product__web_id="123456789",
        brand__name="new_name",
    )
    assert new_product.sku == "123456789"
    assert new_product.upc == "123456789"
    assert new_product.product_type.name == "new_name"
    assert new_product.product.web_id == "123456789"
    assert new_product.brand.name == "new_name"
    assert new_product.is_active == 1
    assert new_product.retail_price == 97.00
    assert new_product.store_price == 92.00
    assert new_product.sale_price == 46.00
    assert new_product.weight == 987


def test_inventory_db_producttype_insert_data(db, product_type_factory):

    new_type = product_type_factory.create(name="demo_type")
    assert new_type.name == "demo_type"


def test_inventory_db_producttype_uniqueness_integrity(
    db, product_type_factory
):
    product_type_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        product_type_factory.create(name="not_unique")


def test_inventory_db_brand_insert_data(db, brand_factory):

    new_brand = brand_factory.create(name="demo_brand")
    assert new_brand.name == "demo_brand"


def test_inventory_db_brand_uniqueness_integrity(db, brand_factory):
    brand_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        brand_factory.create(name="not_unique")


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_inventory, image, alt_text, is_feature, created_at, updated_at",
    [
        (
            1,
            1,
            "images/default.png",
            "a default image solid color",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            8616,
            8616,
            "images/default.png",
            "a default image solid color",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_db_media_dataset(
    db,
    db_fixture_setup,
    id,
    product_inventory,
    image,
    alt_text,
    is_feature,
    created_at,
    updated_at,
):
    result = models.Media.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.product_inventory.id == product_inventory
    assert result.image == image
    assert result.alt_text == alt_text
    assert result.is_feature == is_feature
    assert result_created_at == created_at
    assert result_updated_at == updated_at


def test_inventory_db_media_insert_data(db, media_factory):
    new_media = media_factory.create(product_inventory__sku="123456789")
    assert new_media.product_inventory.sku == "123456789"
    assert new_media.image == "images/default.png"
    assert new_media.alt_text == "a default image solid color"
    assert new_media.is_feature == 1


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_inventory, last_checked, units, units_sold",
    [
        (1, 1, "2021-09-04 22:14:18", 135, 0),
        (8616, 8616, "2021-09-04 22:14:18", 100, 0),
    ],
)
def test_inventory_db_stock_dataset(
    db,
    db_fixture_setup,
    id,
    product_inventory,
    last_checked,
    units,
    units_sold,
):
    result = models.Stock.objects.get(id=id)
    result_last_checked = result.last_checked.strftime("%Y-%m-%d %H:%M:%S")
    assert result.product_inventory.id == product_inventory
    assert result_last_checked == last_checked
    assert result.units == units
    assert result.units_sold == units_sold


def test_inventory_db_stock_insert_data(db, stock_factory):
    new_stock = stock_factory.create(product_inventory__sku="123456789")
    assert new_stock.product_inventory.sku == "123456789"
    assert new_stock.units == 2
    assert new_stock.units_sold == 100


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, description",
    [
        (1, "men-shoe-size", "men shoe size"),
    ],
)
def test_inventory_db_product_attribute_dataset(
    db, db_fixture_setup, id, name, description
):
    result = models.ProductAttribute.objects.get(id=id)
    assert result.name == name
    assert result.description == description


def test_inventory_db_product_attrubite_insert_data(
    db, product_attribute_factory
):
    new_attribute = product_attribute_factory.create()
    assert new_attribute.name == "attribute_name_0"
    assert new_attribute.description == "description_0"


def test_inventory_db_product_attrubite_uniqueness_integrity(
    db, product_attribute_factory
):
    product_attribute_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        product_attribute_factory.create(name="not_unique")


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_attribute, attribute_value",
    [
        (1, 1, 10),
    ],
)
def test_inventory_db_product_attribute_dataset(
    db, db_fixture_setup, id, product_attribute, attribute_value
):
    result = models.ProductAttributeValue.objects.get(id=1)
    assert result.product_attribute.id == 1
    assert result.attribute_value == "10"


def test_inventory_db_product_attribute_value_data(
    db, product_attribute_value_factory
):
    new_attribute_value = product_attribute_value_factory.create(
        attribute_value="new_value", product_attribute__name="new_value"
    )
    assert new_attribute_value.attribute_value == "new_value"
    assert new_attribute_value.product_attribute.name == "new_value"


def test_inventory_db_insert_inventory_product_values(
    db, product_with_attribute_values_factory
):

    new_inv_attribute = product_with_attribute_values_factory(sku="123456789")
    result = models.ProductInventory.objects.get(sku="123456789")
    count = result.attribute_values.all().count()
    assert count == 2
