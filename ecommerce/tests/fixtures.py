import pytest
from django.contrib.auth.models import User
from django.core.management import call_command


@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return a Django admin user.
    """
    return django_user_model.objects.create_superuser("admin", "password")


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    """
    Load DB data fixtures.
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "db_product_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
