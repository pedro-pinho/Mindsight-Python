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
To check coverage of tests with pretty interface run

```shell
coverage run manage.py test
coverage html
```

Then go to htmlcov folder and double click on 'index.html'

Last time runned, report

```shell
---------------------------------------------------------------
MindsightPython\__init__.py                     0      0   100%
MindsightPython\api\__init__.py                 0      0   100%
MindsightPython\api\admin.py                    6      0   100%
MindsightPython\api\models.py                  28      0   100%
MindsightPython\api\serializers.py             37      6    84%
MindsightPython\api\tests.py                  105      0   100%
MindsightPython\api\urls.py                     5      0   100%
MindsightPython\api\views.py                   31     14    55%
MindsightPython\core\__init__.py                0      0   100%
MindsightPython\core\admin.py                   1      0   100%
MindsightPython\core\exception_handler.py      10      3    70%
MindsightPython\core\models.py                  1      0   100%
MindsightPython\core\tests.py                   1      0   100%
MindsightPython\core\urls.py                    8      0   100%
MindsightPython\core\views.py                  11      0   100%
MindsightPython\settings.py                    28      0   100%
MindsightPython\urls.py                         5      0   100%
manage.py                                       9      2    78%
---------------------------------------------------------------
TOTAL                                         286     25    91%
```
