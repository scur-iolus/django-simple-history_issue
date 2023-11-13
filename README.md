# Issue

## Reference

See issue [#1278](https://github.com/jazzband/django-simple-history/issues/1278) on the django-simple-history official repo.

## Steps to reproduce

Using `pipenv`:

```bash
pipenv install -r requirements.txt
cd mysite
# then the following commands will work fine, although I think an error should be raised
python manage.py makemigrations
python3 manage.py test

```
