# setup-for-django-ecommerce-part-8
A little help you get you started

1. Download code and open in your preferred code editor
2. Create a Virtual Environment. If you are using Visual Studio Code, open the terminal and type:

### Windows
```
py -m venv venv
```
### Mac
```
virtualenv venv
```

3. Activate venv

### Windows
```
py venv\Scripts\activate
```
### Mac
```
source  venv/bin/activate
```

4. Now install the dependencies

```
pip install -r dev-requirements.txt
```

5. You will need docker for this project. Go ahead and install docker desktop if you havent already done so

6. Start the new containers

```
docker-compose up -d
```

7. Now install the fixtures (the data for the database). This will take some time because they are very large 200.000+ rows. Fixtures are found <a href="https://github.com/veryacademy/fixtures-django-ecommerce-part-7"> here </a> Download the fixtures and put the fixture folder in the following folder /ecommerce/demo/ To confirm there should be a folder named fixture now in the demo app folder, inside of the fixture folder is around 10 files. 

8. Now you can load the fixtures into the database (remember this will take a while and will show a warning - its ok just ignore)

### Windows
```
py manage.py demo-fixtures
```
### Mac
```
python3 manage.py demo-fixtures
```

9. Start the server and check it out

### Windows
```
py manage.py runserver
```
### Mac
```
python3 manage.py runserver
```