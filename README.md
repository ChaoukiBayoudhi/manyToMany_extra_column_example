# Many To Many extra column example

A Django project with 3 models and a REST API (Django REST Framework).

## Tech stack

- Python 3
- Django
- Django REST Framework
- Database: SQLite

## Project structure

- `manyToMany_extra_column_example/`: project settings and root URLs
- `store_app/`: Django app
- Tests: `store_app/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Client` | `store_app` | name, address, email, telephone |
| `Product` | `store_app` | label, price, stock, clients |
| `Command` | `store_app` | client, product, quantity, date |

## URL routes

Declared in `urls.py`:

- `/blog/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

There is no `requirements.txt`; the packages above are the ones the settings and imports refer to.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
