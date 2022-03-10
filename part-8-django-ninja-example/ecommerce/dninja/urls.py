from django.urls import path
from ecommerce.dninja.api import api

urlpatterns = [
    path("", api.urls)
]