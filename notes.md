# E-commerce V2

# Pytest

pytest -m "not selenium" -rP


# Topics Covered

- Creating custom fields 
cas = models.CharField(max_length=11, validators=[RegexValidator(r'^\d\d-\d\d-\d\d-\d\d$')])


Make Password Fixture
---
```
./manage.py shell

from django.contrib.auth.hashers import make_password
make_password('password')


# Load fixture
manage.py loaddata en_fixture
```

\docs>make html

https://django-ecommerce-project-v2.readthedocs.io/en/latest/


Dataset
---
https://www.kaggle.com/datafiniti/womens-shoes-prices