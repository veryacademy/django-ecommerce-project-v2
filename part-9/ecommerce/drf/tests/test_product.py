import json

from .utils import convert_to_dot_notation


def test_get_product_by_category(api_client, single_product):
    product = single_product
    endpoint = f"/api/inventory/products/category/{product.category}/"
    response = api_client().get(endpoint)
    expected_json = [
        {
            "name": product.name,
            "web_id": product.web_id,
        }
    ]
    assert response.status_code == 200
    assert response.data == expected_json


def test_get_inventory_by_web_id(api_client, single_sub_product_with_media_and_attributes):
    fixture = convert_to_dot_notation(single_sub_product_with_media_and_attributes)

    endpoint = f"/api/inventory/{fixture.inventory.product.web_id}/"
    response = api_client().get(endpoint)

    expected_json = [
        {
            "id": fixture.inventory.id,
            "sku": fixture.inventory.sku,
            "store_price": fixture.inventory.store_price,
            "is_default": fixture.inventory.is_default,
            "brand": {"name": fixture.inventory.brand.name},
            "product": {
                "name": fixture.inventory.product.name,
                "web_id": fixture.inventory.product.web_id,
            },
            "promotion_price": None,
            "weight": fixture.inventory.weight,
            "media": [
                {
                    "img_url": fixture.media.img_url.url,
                    "alt_text": fixture.media.alt_text,
                }
            ],
            "attributes": [
                {
                    "attribute_value": fixture.attribute.attribute_value,
                    "product_attribute": {
                        "id": fixture.attribute.id,
                        "name": fixture.attribute.product_attribute.name,
                        "description": fixture.attribute.product_attribute.description,
                    },
                }
            ],
            "product_type": fixture.inventory.product_type.id,
        }
    ]

    assert response.status_code == 200
    assert json.loads(response.content) == expected_json
