def test_get_all_categories(c_client, category_with_multiple_children):
    endpoint = "/ninja/inventory/category/all/"
    response = c_client().get(endpoint)
    assert response.status_code == 200
    response.content
