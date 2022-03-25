pytest_plugins = [
    "ecommerce.tests.inventory_fixtures",
    "ecommerce.tests.promotion_fixtures",
    "ecommerce.tests.api_client",
    "celery.contrib.pytest",
]
