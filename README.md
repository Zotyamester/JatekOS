# JátékOS

## Előfeltételek

A szerver működtetéséhez **Python 3.9** (vagy újabb) szükséges.

## Telepítés

### Python

```sh
pip install django django-crispy-forms djangorestframework channels pillow

cd mysite/

python manage.py makemigrations main accounts groups games posts chat

python manage.py migrate

python manage.py loaddata games

python manage.py createsuperuser
```

## Környezeti változók

Az e-mailezés működéséhez szükséges beállítani az EMAIL_HOST_USER-t és az EMAIL_HOST_PASSWORD-öt egy-egy környezeti változóként.

## Futtatás

```sh
cd mysite/

python manage.py runsever 0.0.0.0:6969
```

## Dokumentáció

A gyökérmappában található meg _Dokumentáció.pdf_ néven.
