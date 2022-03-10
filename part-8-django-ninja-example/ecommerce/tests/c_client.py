import pytest
from django.test import Client


@pytest.fixture
def c_client():
    return Client
