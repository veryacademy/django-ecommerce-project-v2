import sys
import time
from time import sleep

import pytest
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# @pytest.fixture
# def admin_user(db):
#     """Return a Django admin user."""
#     return User.objects.create_superuser("admin", "password")


# Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(chrome_options=options)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture
def test_new_user(django_user_model):
    """Return a Django admin user."""
    return django_user_model.objects.create_superuser("admin", "password")
