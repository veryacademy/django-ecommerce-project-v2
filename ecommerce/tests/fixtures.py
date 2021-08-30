import pytest
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# @pytest.fixture
# def admin_user(db):
#     """Return a Django admin user."""
#     return User.objects.create_superuser("admin", "password")


@pytest.fixture(scope="module")
def browser(request):
    """Provide a selenium webdriver instance."""
    options = Options()
    options.headless = False
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    browser.close()


@pytest.fixture
def test_new_user(django_user_model):
    """Return a Django admin user."""
    return django_user_model.objects.create_superuser("admin", "password")
