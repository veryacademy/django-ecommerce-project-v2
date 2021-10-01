import pytest
from django.contrib.auth.models import User
from django.core.management import call_command
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    Provide a selenium webdriver instance.
    """
    options = Options()
    options.headless = False
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    browser.close()


@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return a Django admin user.
    """
    return django_user_model.objects.create_superuser("admin", "password")


# @pytest.fixture
# def admin_user(db):
#     """Return a Django admin user."""
#     return User.objects.create_superuser("admin", "password")


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    """
    Setup DB data fixtures.
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "db_product_2.json")
