import pytest
from ecommerce.inventory.models import Product


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
