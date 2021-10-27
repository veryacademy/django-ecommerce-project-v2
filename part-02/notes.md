# E-commerce V2

# Pytest
```
pytest -m "not selenium" -rP
```

## Creating custom fields 
```
cas = models.CharField(max_length=11, validators=[RegexValidator(r'^\d\d-\d\d-\d\d-\d\d$')])
```

## PowerShell - Prepare fixtures
```
$topicsjson = import-csv .\db_product_inventory.csv | ConvertTo-Json
$topicsjson | Add-Content -Path "mydata.json"
```

## Make Password Fixture
---
```
./manage.py shell

from django.contrib.auth.hashers import make_password
make_password('password')
```

## Load fixture
```
manage.py loaddata xyz.json
manage.py dumpdata auth.user --indent 2 > user.json 
```

## Docs
```
\docs>make html
```
```
https://django-ecommerce-project-v2.readthedocs.io/en/latest/
```


## Dataset
```
https://www.kaggle.com/datafiniti/womens-shoes-prices
```