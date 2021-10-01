def test_admin_str(create_admin_user):
    assert create_admin_user.__str__() == "admin"
