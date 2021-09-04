# E-commerce V2





# Topics Covered

- Creating custom fields 
cas = models.CharField(max_length=11, validators=[RegexValidator(r'^\d\d-\d\d-\d\d-\d\d$')])




# Topics

1.0 Product Inventory

1. First Normal Form
2. Second Normal Form



2NF

But it is not yet in 2NF. If student 1 leaves university and the tuple is deleted, then we loose all information about professor Schmid

http://www.gitta.info/LogicModelin/en/html/DataConsiten_Norm2NF.html
3NF
https://www.youtube.com/watch?v=_K7fcFQowy8
Relationships
https://www.lifewire.com/database-relationships-p2-1019758
https://www.amazon.co.uk/Under-Armour-Sport-Style-Short-Sleeve/dp/B077XQ3L47/ref=zg_bs_1731028031_21?_encoding=UTF8&psc=1&refRID=7M2AH11KFP8X6DQJ6EJY
Bibliography
https://www.gs1uk.org/get-a-barcode?gclid=Cj0KCQjwjo2JBhCRARIsAFG667VMFABlLuVZ_T3hArKMcC_n7zX44ZpjzZhZm1fdJ9q0_DiLyi_WFB4aAlehEALw_wcB




Make Password Fixture
---
```
./manage.py shell

from django.contrib.auth.hashers import make_password
make_password('password')


#json fixture file
'pbkdf2_sha256$10000$vkRy7QauoLLj$ry+3xm3YX+YrSXbri8s3EcXDIrx5ceM+xQjtpLdw2oE='

[
    { "model": "auth.user",
        "pk": 1,
        "fields": {
            "username": "admin",
            "password": "pbkdf2_sha256$260000$jXc6ssvKJLcIvSKHecU9xH$67RkA/yGarazwLD1666HQZDygbIu2V6i1x2yFBVGk/0="
            "is_superuser": true,
            "is_staff": true,
            "is_active": true
        }
    }
]

# Load fixture
manage.py loaddata en_fixture
```

\docs>make html

https://django-ecommerce-project-v2.readthedocs.io/en/latest/


Dataset
---
https://www.kaggle.com/datafiniti/womens-shoes-prices