# Wedding-CMS

## Requirements
* [pyenv](https://github.com/pyenv/pyenv) + [pipenv](https://pypi.org/project/pipenv/) on python 3.8 or later

### Backend

Run the dev django app:
```shell script
pipenv run python manage.py runserver
```

Apply db migrations:
```shell script
pipenv run python manage.py migrate
```

Add a initial superuser:
```shell script
pipenv run python manage.py createsuperuser
```
