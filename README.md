# Mindsight-Python

To start, run

```shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Then go to

[localhost:8000](127.0.0.1:8000)

---

## Available routes

* [List] : `GET /employees/`
* [Register] : `POST /employees/`
* [Descendants] : `GET /employees/{employee_name}`

---
To run tests

```shell
python manage.py test
```

---
To check coverage of the tests

```shell
coverage run manage.py test
coverage html
```

Then go to htmlcov folder and double click on 'index.html'
