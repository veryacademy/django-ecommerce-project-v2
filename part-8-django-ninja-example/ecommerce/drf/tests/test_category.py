from urllib import response


def test_get_all_categories(api_client, category_with_multiple_children):
    endpoint = "/api/inventory/category/all/"
    response = api_client().get(endpoint)
    assert response.status_code == 200
    assert len(response.data) == len(category_with_multiple_children)
