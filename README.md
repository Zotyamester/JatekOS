# JatekOS

## Prerequisites

**Python 3.9** (or later) is required to run the server.

## Installation

### Python

```sh
pip install django django-crispy-forms djangorestframework channels pillow

cd mysite/

python manage.py makemigrations main accounts groups games posts chat

python manage.py migrate

python manage.py loaddata games

python manage.py createsuperuser
```

## Environment variables

For email to work, setting EMAIL_HOST_USER and EMAIL_HOST_PASSWORD as environment variables is necessary.

## Run

```sh
cd mysite/

python manage.py runserver 0.0.0.0:6969
```

## Documentation

It is located in the root folder as _documentation.pdf_.
