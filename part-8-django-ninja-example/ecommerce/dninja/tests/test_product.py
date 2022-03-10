import json


def test_get_product_by_category(c_client, single_product):
    product = single_product
    endpoint = f"/ninja/inventory/products/category/{product.category}/"
    response = c_client().get(endpoint)
    assert response.status_code == 200
