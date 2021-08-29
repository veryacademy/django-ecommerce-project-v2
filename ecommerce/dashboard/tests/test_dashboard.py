def test_customer_str(test_new_user):
    assert test_new_user.__str__() == "admin"
