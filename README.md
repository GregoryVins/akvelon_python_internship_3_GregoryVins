# akvelon_python_internship_3_GregoryVins

- [Technical task](https://docs.google.com/document/d/1rQhDZzebDDJ6c-__P8LkUH0HvwT0qCXyDUbqks7DJlg/edit?usp=sharing) - If you want to know the initial conditions
- [@GregoryVins](https://t.me/GregoryVins) - If you want to say something


Get started
-----------
Get started with docker:
```
docker-compose up
```

To run from local computer:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Generate data
-------------
To quickly filling the database with random objects
```
python manage.py create_users
python manage.py create_transactions
```
To drop all database objects use:
```
python manage.py delete_users
python manage.py delete_transactions
```